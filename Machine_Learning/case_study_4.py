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