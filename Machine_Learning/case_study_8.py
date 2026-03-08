import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

#########################################################
# Step 1 : Load the dataset
#########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial entries from dataset :")
print(df.head())

#########################################################
# Step 2 : Data Analysis (EDA)
#########################################################

print(Border)
print("Step 2 : Data analysis")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["species"].value_counts())

print("Statistical Report of dataset")
print(df.describe())


#########################################################
# Step 3 : Decide Independetn and Dependent Variable
#########################################################

print(Border)
print("Step 3 : Decide Independetn and Dependent Variable")
print(Border)


# X: Independent variables/features
# Y: Dependent Varibale/Labels
feature_call=["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"]
X=df[feature_call]
Y=df["species"]

print(f"X shape {X.shape}")
print(f"Y shape {Y.shape}")

#########################################################
# Step 4 : Visualisation of Dataset
#########################################################

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

#Sctattered  plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp=df[df["species"]==sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp)

plt.title("Iris : Petal Length vs Petal Width")
plt.xlabel("Petal Length cm")
plt.ylabel("Petal Width cm")
plt.legend()
plt.grid(True)
plt.show()


#########################################################
# Step 5 : Split the Dataset
#########################################################

print(Border)
print("Step 5 : Split the  Dataset")
print(Border)

#total dataset=150,5
#X: 150,4
# Y: 150,1
#test size=20%
#train size=80%
# random_state=
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
print(F"Data spilitting activity Done")
print(F"X_train: {X_train.shape}")
print(F"Y_train: {Y_train.shape}")
print(F"X_test: {X_test.shape}")
print(F"Y_test {Y_test.shape}")


#########################################################
# Step 6 : Build the model
#########################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

print("We are going to use DecisionTreeClassifier")
model=DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model Successfully created : ",model)

#########################################################
# Step 7 : Train the model
#########################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model training completed")



#########################################################
# Step 8 : Evaluate the model
#########################################################

print(Border)
print("Step 8 : Evaluate the model")
print(Border)

Y_pred=model.predict(X_test)

print(f"Model Evaluation Complete(testing)")
print(Y_pred.shape)

print("Expected Answer: ")
print(Y_test)
print("Predicted Answer")
print(Y_pred)