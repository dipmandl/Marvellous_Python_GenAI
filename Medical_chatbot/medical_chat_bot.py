from gpt4all import GPT4All
import json
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# -------------------------------
# 1️⃣ Load GPT4All Model
# -------------------------------
MODEL_PATH = "ggml-gpt4all-l13b-snoozy.bin"  # path to your downloaded GPT4All model
model = GPT4All(MODEL_PATH)

# -------------------------------
# 2️⃣ Load Medical Knowledge Base
# -------------------------------
with open("medical_tests.json", "r") as f:
    medical_data = json.load(f)

# -------------------------------
# 3️⃣ Build Embeddings + FAISS Index
# -------------------------------
embed_model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight offline model

# Combine test_name + description + precautions for embeddings
documents = []
for item in medical_data:
    text = f"{item['test_name']}: {item['description']}. Precautions: {', '.join(item['precautions'])}"
    documents.append(text)

# Create embeddings
embeddings = embed_model.encode(documents, convert_to_numpy=True)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# -------------------------------
# 4️⃣ Retrieval Function
# -------------------------------
def retrieve_relevant(user_query, top_k=1):
    # If user query is very short (like "ECG"), expand it
    if len(user_query.split()) <= 2:
        user_query = f"Tell me about {user_query}"

    query_vec = embed_model.encode([user_query], convert_to_numpy=True)
    distances, indices = index.search(query_vec, top_k)
    results = [documents[i] for i in indices[0]]
    return results

# -------------------------------
# 5️⃣ Chat Loop
# -------------------------------
print("Medical RAG Chatbot (offline). Type 'exit' to quit.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Exiting chatbot...")
        break

    # Retrieve relevant context
    retrieved_info = retrieve_relevant(user_input, top_k=1)
    context = "\n".join(retrieved_info)

    # Build prompt for GPT4All
    prompt = f"""
You are a helpful medical assistant. Use the context below to answer user questions.
Provide:
1. Test description
2. Precautions before the test
3. Additional tips if applicable

Context:
{context}

User Question: {user_input}
"""

    # Generate answer
    response = model.generate(prompt)
    print(f"Bot: {response}\n")