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
    print("Step 1 : Load the content")
    print(border)
    df=pd.read_csv(DataPath)

    print("Few Records from dataset: ")
    print(df.head())
    # --------------------------------------------------------
    # Step 2: Remove Unwanted Column
    # --------------------------------------------------------
    print(border)
    print("Step 2 : Removed Unwanted Column")
    print(border)

    print("Shape of DataSet Before Remove")
    print(df.shape)
    print("Correlation Matrix:")
    print(df.corr())
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
    print("Step 3 : Check Missing Values")
    print(border)

    print("Missing Values Count:\n",df.isnull().sum())

    # --------------------------------------------------------
    # Step 4: Display Statistical Summary
    # --------------------------------------------------------
    print(border)
    print("Step 4 : Display Statistical Summary")
    print(border)
    print(df.describe())

    # --------------------------------------------------------
    # Step 5: Correlation between columns
    # --------------------------------------------------------
    print(border)
    print("Step 5 : Correlation between columns")
    print(border)
    print("Correlation Matrix:")
    print(df.corr())

    # --------------------------------------------------------
    # Step 6: Split Dataset Into Independent and Dependent Variables
    # --------------------------------------------------------
    print(border)
    print("Step 6 : Split Dataset Into Independent and Dependent Variables")
    print(border)
    X=df[['TV','radio','newspaper']]
    Y=df['sales']
    print(f"Shape of Independent Varibale:\n {X.shape}")
    print(f"Shape of Dependent Varibale:\n {Y.shape}")

    # --------------------------------------------------------
    # Step 7: Split Dataset for training and testing
    # --------------------------------------------------------
    print(border)
    print("Step 7 : Split Dataset for training and testing")
    print(border)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.1)

    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"Y_train shape: {Y_train.shape}")
    print(f"Y_test shape: {Y_test.shape}")

    # --------------------------------------------------------
    # Step 8 : Create the model
    # --------------------------------------------------------
    print(border)
    print("Step 8 : Create and train the model")
    print(border)
    model=LinearRegression()
    model.fit(X_train,Y_train)

    # --------------------------------------------------------
    # Step 9 : Test The Model
    # --------------------------------------------------------
    print(border)
    print("Step 9 : Test The Model")
    print(border)
    Y_pred=model.predict(X_test)

    # --------------------------------------------------------
    # Step 10 : Evaluate The Model
    # --------------------------------------------------------
    print(border)
    print("Step 10 : Evaluate The Model")
    print(border)

    MSE=mean_squared_error(Y_test,Y_pred)
    RSME=np.sqrt(MSE)

    R2=r2_score(Y_test,Y_pred)

    print(f"Mean Squared Error: {MSE}")
    print(f"Root Mean Squared Error: {RSME}")
    print(f"R Square Value: {R2}")

    # --------------------------------------------------------
    # Step 11 : Calculate model coefficient
    # --------------------------------------------------------
    print(border)
    print("Step 11 : Calculate model coefficient")
    print(border)

    for col,val in zip(X.columns,model.coef_):
        print(f"{col} : {val}")

    print(f"\nIntercept: {model.intercept_}")

    # --------------------------------------------------------
    # Step 12 : Compare the actual and predicted values
    # --------------------------------------------------------
    print(border)
    print("Step 12 : Compare the actual and predicted values")
    print(border)

    result=pd.DataFrame({'Actual Sale':Y_test.values,
                         'Predicted Sale':Y_pred
                         })
    print(result.head())

    # --------------------------------------------------------
    # Step 13 : Plot actual vs predicted
    # --------------------------------------------------------
    print(border)
    print("Step 13 : Plot actual vs predicted")
    print(border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Actual Sales vs Predicted Sales")
    plt.grid(True)
    plt.show()



def main():
    MarvellousAdverise("Advertising.csv")

if __name__=='__main__':
    main()
