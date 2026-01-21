# Q1: check number is prime or not
#input 11 prime number
def check_prime(n1):
    Flag=True
    for i in range(2,n1):
        if n1%i==0:
            Flag=False
            break
    if Flag==True:
        print(n1," Is prime number")
    else:
        print(n1," Not prime number")
# Q2: counts digit in numbers
# input 125534  output=6
def checkLength(n1):
    print("Lenght of ",n1,"is: ",len(str(n1)))

# Q3: print sum of digit
# input 123  output 6
def sumDigit(n1):
    sum=0
    n=str(n1)
    for i in range(0,len(n)):
        sum=sum+int(n[i])
    print("Sum of Digit of ",n1,"Is ",sum)

# Q4: print revers of that number
#input 123  output 321
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print("Reverse of ",n,"IS: ",rev)

# Q5: check number is pallindrome or not
#input 121  output pallindrome

def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__=="__main__":
    check_prime(11)
    checkLength(1562)
    sumDigit(1234)
    reverse_number(123)
    palindrome(121)

# OUTPUT:
# PS C:\Users\91951\Desktop\Python\Marvellous_Python_GenAI\Assignments> python .\Assignment_11.py
# 11  Is prime number
# Lenght of  1562 is:  4
# Sum of Digit of  1234 Is  10
# Reverse of  123 IS:  321
# 121 Pallindrome
