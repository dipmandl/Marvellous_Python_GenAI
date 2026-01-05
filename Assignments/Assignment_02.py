#Q1: Write a program to display value, type and memory adrress:
a=10
#value:
print(a)
#type
print(type(a))
#memory address
print(id(a))

#output:
# 10
# <class 'int'>
# 2261194074704




#Q2: what is difference between a=10, b=10 and a=[10],b=[10]
a=10
b=10
#both are assign to integer datatype by python internal system.
#when the are created they assign to same memory address.
print("memory of a: ",id(a))
print("memory of b: ",id(b))
#where as
a=[10]
b=[10]
print("memory of a: ",id(a))
print("memory of b: ",id(b))
#both are assign to list datatype by python internal system.
#when the are created they assign to different memory address.

#OUTPUT:
# memory of a:  1907917548112
# memory of b:  1907917548112
# memory of a:  1907923645376
# memory of b:  1907923648320


#Q3: what does id function return:
#id() function is returning the memory address for the object in python.

#Q4:  what is purpose of getsizeof()?
#getsizeof will return the memory size in byte

#Q5: predict the ouput:
a=10
b=10
print(id(a)==id(b))
#output True
#id() function is return the memory address and == is used for comparision
#when storing same value in immutable object python assign the same memory address to them.

# Q6: write a program which accept 2 number and print addition,subtraction,multiplication,division
n1=int(input("Enter no1: "))
n2=int(input("Enter no2: "))
print("Addition is : ",n1+n2)
print("Subtraction is : ",n1-n2)
print("Multiplication is : ",n1*n2)
print("Division is : ",n1/n2)


#OUTPUT:
# Enter no1: 10
# Enter no2: 5
# Addition is :  15
# Subtraction is :  5
# Multiplication is :  50
# Division is :  2.0


#Q7: why input always return string:
# Python is dynamically type langauge, so when accepting the input it cannot guess the wheather
# its string,float or int. so It will consider all as a string and then as per user
# action we can convert into int float etc and that is called typecasting

# Q8:predict the output:
x=input("enter number")
print(type(x))

#It will return <class str> because python  input function always return string

# OUTPUT:
# <class 'str'>



#Q9: write a program to take username and age and display
# Hello <name>, you will turn <age+1> next year.
name=input("enter name: ")
age=int(input("enter age: "))

print("Hello "+ name+", you will turn "+str(age+1)+" next year.")
#
# Output:
# enter name: dip
# enter age: 23
# Hello dip, you will turn 24 next year.


# Q10: What will be the output and explain difference:
print("10"+"20")
print(10+20)

#in Python + is used for concatenation of string as well as arithmetic operation
# so in first case both are the string so it will print 1020
#second case both will consider as integer and print 30
# but in one more scenario if we pass print(10+"30")  it will give an error
#because concatenation will work with only string
#and arithemtic will not work with string.