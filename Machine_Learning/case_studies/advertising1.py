import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



def main():

    df=pd.read_csv('Advertising.csv')
    print(df.shape)  #(200,5)
    # Data Cleaning
    if 'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0',inplace=True)
    print(df.shape)  #(200,4)


if __name__=='__main__':
    main()