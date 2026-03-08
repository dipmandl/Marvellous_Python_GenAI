#   [A,B,C,D]
# X=[1,2,3,5]
# Y=[2,3,1,6]
#   [R,R,B,B]

#predict (3,3) what will be the value.

def MarvellousKNeighborsClassifier():
    border="-"*40
    data=[{'point':'A','X':1,'Y':2,'Label':'Red'},
          {'point':'B','X':2,'Y':3,'Label':'Red'},
          {'point':'C','X':3,'Y':1,'Label':'Blue'},
          {'point':'D','X':5,'Y':6,'Label':'Blue'}
          ]

    print(border)
    print("Marvellous user Define KNN: ")
    print(border)

    print("\n\n"+border)
    print("Training Data Set")
    print(border)

    for i in data:
        print(i)

    print(border)

def main():
    MarvellousKNeighborsClassifier()


if __name__=="__main__":
    main()