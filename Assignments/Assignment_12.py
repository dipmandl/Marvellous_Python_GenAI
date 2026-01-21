# Q1: Write a program which accept the character and print its vowel or consonants
def checkChar(ch):
    if ch in ('a','e','i','o','u','A','E','I','O','U'):
        print(ch," Is Vowel")
    else:
        print(ch, " Is Consonants")

# Q2: Write a program which accept number and print its factor
def printFactors(n1):
    for i in range(1,n1+1):
        if n1%i==0:
            print(i)


# Q3: Write a program which accept 2 numbers and print addition,subtraction,multiplication,Division
def printArith(n1,n2):
    print("Addtion is: ",n1+n2)
    print("Subtraction is: ",n1-n2)
    print("Multiplication is: ",n1*n2)
    print("Division is: ",n1/n2)

# Q4: Write a program which accept a number and print that many starting from 1
def printNum(n1):
    for i in range(1,n1+1):
        print(i)
# Q5: Write a program which accept number and print that will in reverse order
def printNumRev(n1):
    print("Reverse")
    for i in range(n1,0,-1):
        print(i)


if __name__=="__main__":
    checkChar('K')
    checkChar('o')
    printFactors(12)
    printFactors(21)
    printArith(12,10)
    printNum(12)
    printNumRev(12)



# OUTPUT:
# PS C:\Users\91951\Desktop\Python\Marvellous_Python_GenAI\Assignments> python .\Assignment_12.py
# K  Is Consonants
# o  Is Vowel
# 1
# 2
# 3
# 4
# 6
# 12
# 1
# 3
# 7
# 21
# Addtion is:  22
# Subtraction is:  2
# Multiplication is:  120
# Division is:  1.2
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# Reverse
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
