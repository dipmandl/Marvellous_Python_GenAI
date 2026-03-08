from sklearn.metrics import r2_score

def main():
    Y_actual=[3,4,2,4,5]   #Y
    Y_predcited=[1.8,1.2,3.6,1.0,2.4]    #Yp

    r2=r2_score(Y_actual,Y_predcited)
    print(f"Actual Values Y: {Y_actual}")
    print(f"Predicted Values Yp: {Y_predcited}")
    print(f"R :{r2}")  #0.3076


if __name__=="__main__":
    main()