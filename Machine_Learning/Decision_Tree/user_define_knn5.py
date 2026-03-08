#   [A,B,C,D]
# X=[1,2,3,5]
# Y=[2,3,1,6]
#   [R,R,B,B]
import math

#predict (3,3) what will be the value.

import numpy as np
from math import sqrt

def Eucdistance(p1,p2):
    ans=sqrt((p2['X']-p1['X'])**2+(p2['Y']-p1['Y'])**2)
    return ans



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

    new_point={'X':3,'Y':3}
    #calculate all distance
    for d in data:
        d['distance']=Eucdistance(d,new_point)

    print(border)
    print("Calculated Distances are")
    print(border)
    for i in data:
        print(i)
    print(border)

    sorted_data=sorted(data,key=lambda item: item['distance'])

    print(border)
    print("Sorted Data")
    for i in sorted_data:
        print(i)
    print(border)

    k=3
    nearest=sorted_data[:k]
    print(border)
    print("Nearest 3 Elements Are")
    for i in nearest:
        print(i)
    print(border)

    #voting:
    votes={}
    for neighbor in nearest:
        Label=neighbor['Label']
        votes[Label]=votes.get(Label,0)+1

    print(border)
    print("voting Result ")
    print(border)
    for d in votes:
        print(f"Name: {d} Value: {votes[d]}")

    print(border)

    predicted_class=max(votes,key=votes.get)
    print("Predicted Class of (3,3) is: ")
    print(predicted_class)
    print(border)


def main():
    MarvellousKNeighborsClassifier()


if __name__=="__main__":
    main()