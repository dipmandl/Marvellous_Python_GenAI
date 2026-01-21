# Q1: write a which accept one number and print multiplication table for that number
def printTable(n1):
    mult=1
    for i in range(1,11):
        mult=i*n1
        print(mult)



# Q2: write a program which accept one number and print the sum of first n natural numbers
def printSum(n1):
    sum=0
    for i in range(1,n1+1):
        sum=sum+i
    print("Sum: ",sum)

# Q3: write a program which accept one number and print the factorial of the number
def printFactorial(n1):
    fact=1
    for i in range(1,n1+1):
        fact=fact*i
    print("Factorial: ",fact)

# Q4: write a program which accpet one number and all even numbers till that number
def printEven(n1):
    for i in range(2,n1+1):
        if i%2==0:
            print(i)


# Q5: write a program which accpet one number and all odd numbers till that number
def printOdd(n1):
    odd=[]
    for i in range(2,n1+1):
        if i%2!=0:
            print(i)



if __name__=="__main__":
    n1=int(input(("Enter Number on which you need to perform operations: ")))
    print("Printing Table for: ",n1)
    printTable(n1)
    print("Printing Sum Till : ", n1)
    printSum(n1)
    print("Printing Factorial for: ", n1)
    printFactorial(n1)
    print("Printing Even Numbers Till : ", n1)
    printEven(n1)
    print("Printing Odd Number Till: ", n1)
    printOdd(n1)



# OUTPUT:
# PS C:\Users\91951\Desktop\Python\Marvellous_Python_GenAI\Assignments> python .\Assignment_10.py
# Enter Number on which you need to perform operations: 5
# Printing Table for:  5
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# Printing Sum Till :  5
# Sum:  15
# Printing Factorial for:  5
# Factorial:  120
# Printing Even Numbers Till :  5
# 2
# 4
# Printing Odd Number Till:  5
# 3
# 5


# Output2:
# PS C:\Users\91951\Desktop\Python\Marvellous_Python_GenAI\Assignments> python .\Assignment_10.py
# Enter Number on which you need to perform operations: 10
# Printing Table for:  10
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100
# Printing Sum Till :  10
# Sum:  55
# Printing Factorial for:  10
# Factorial:  3628800
# Printing Even Numbers Till :  10
# 2
# 4
# 6
# 8
# 10
# Printing Odd Number Till:  10
# 3
# 5
# 7
# 9



