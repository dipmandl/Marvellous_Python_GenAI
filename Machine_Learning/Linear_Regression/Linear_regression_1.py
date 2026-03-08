import numpy as np
import pandas as pd
import matplotlib as plt

def MarvellousPredictor():
    border="*"*40
    #load the data:
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]
    print(border)
    print("Values of independent variable X: ")
    print(X)
    print("Values of Dependent variable Y: ")
    print(Y)

    mean_x=np.mean(X)
    mean_y=np.mean(Y)
    print(border)
    print(f"X_Mean is : {mean_x} \nY_Mean is: {mean_y}")

def main():
    MarvellousPredictor()

if __name__=="__main__":
    main()