#Q1: write program which contains the display function and print the Jay Ganesh
def Displya():
    print("Jay Ganesh")
#Output:
# python .\Assignment_09.py
# Jay Ganesh
# Q2 Write a program which contains a one function ChkGretare accept 2 parameter and
# print the greatest number:
def ChkGreater(n1,n2):
    if n1>n2:
        print(n1," Is greater")
    else:
        print(n2, " Is greater")
#output
# 12  Is greater

# Q3 write a  program which accept 1 number and print square of that number:
# input 5 outpt 25
def square(n1):
    print(n1**2)
    #also we can do
    print(n1*n1)
#output:
# 25
# 25

# Q 4: Write a program which accept one number and print cube of that number:
def printCube(n1):
    print(n1**3)

#input 5 output 125


# Q5: Write a program which accept one number and check its divisible by 3 and 5
def checkDivisibleBy3(n1):
    if n1%3==0 and n1%5==0:
        print(n1,"Is Divisible by 3 and 5")
    else:
        print(n1,"Is not divisible by 3 and 5")
# Input: 15
# Output: 15 Is Divisible by 3 and 5





if __name__=="__main__":
    Displya()
    ChkGreater(11,12)
    ChkGreater(111, 12)
    square(5)
    square(9)
    printCube(5)
    printCube(4)
    checkDivisibleBy3(15)
    checkDivisibleBy3(21)


# OUTPUT for all the function calls
# PS C:\Users\91951\Desktop\Python\Marvellous_Python_GenAI\Assignments> python .\Assignment_09.py
# Jay Ganesh
# 12  Is greater
# 25
# 25
# 25
# 25
# 81
# 81
# 125
# 64
# 15 Is Divisible by 3 and 5
# 21 Is not divisible by 3 and 5
