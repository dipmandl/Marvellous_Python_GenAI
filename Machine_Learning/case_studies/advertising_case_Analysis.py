import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdverise(DataPath):
    border='-'*40
    #--------------------------------------------------------
    # Step 1: Load Data Set
    #--------------------------------------------------------
    print(border)
    print("Step 1: Load the content")
    print(border)
    df=pd.read_csv(DataPath)

    print("Few Records from dataset: ")
    print(df.head())
    # --------------------------------------------------------
    # Step 2: Remove Unwanted Column
    # --------------------------------------------------------
    print(border)
    print("Step 2: Removed Unwanted Column")
    print(border)

    print("Shape of DataSet Before Remove")
    print(df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of DataSet After Remove")
    print(df.shape)
    print(border)
    print("Clean Dataset: ")
    print(border)
    print(df.head())

    # --------------------------------------------------------
    # Step 3: Check Missing Values
    # --------------------------------------------------------
    print(border)
    print("Step 3: Check Missing Values")
    print(border)

    print("Missing Values Count:\n",df.isnull().sum())

    # --------------------------------------------------------
    # Step 4: Display Statistical Summary
    # --------------------------------------------------------
    print(border)
    print("Step 4: Display Statistical Summary")
    print(border)
    print(df.describe())

    # --------------------------------------------------------
    # Step 5: Correlation between columns
    # --------------------------------------------------------
    print(border)
    print("Step 5: Correlation between columns")
    print(border)
    print("Correlation Matrix:")
    print(df.corr())





def main():
    MarvellousAdverise("Advertising.csv")

if __name__=='__main__':
    main()
