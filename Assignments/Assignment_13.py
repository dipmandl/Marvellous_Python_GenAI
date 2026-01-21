# Q1 Write a program which accept the length and width and print area
def area_of_rectangle(length, width):
    return length * width

# Q2 Write a program accept radius and area of circle
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

# Q3 Write a program accept a number and check wheather its perfect or not
def is_perfect_number(n):
    if n <= 0:
        return False

    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n

# Q4 Write a program accept a number and print its binary equivalent
def binary_equivalent(n):
    return bin(n)[2:]

# Q5 Write a program which accept marks and print grade
def get_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"

if __name__=="__main__":
    res=area_of_rectangle(10,20)
    print("Area of Rectangle is: ",res)
    res=area_of_circle(5)
    print("Area of Circle: ",res)
    res=is_perfect_number(6)
    print("6 is perfect or not: ",res)
    res=get_grade(98)
    print("grade for 98 is: ",res)


#OUTPUT:
# PS C:\Users\91951\Desktop\Python\Marvellous_Python_GenAI\Assignments> python .\Assignment_13.py
# Area of Rectangle is:  200
# Area of Circle:  78.5397
# 5
# 6 is perfect or not:  True
# grade for 98 is:  Distinction




