#Q1: what is userdefined function and write
# a function which accept two numbers and return multiplication
# A user-defined function in Python is a function that you create to perform a specific task,
# syntax:
# def function_name(parameters):
#     # function body
#     return value

def add(a, b):
    return a * b

result = add(3, 5)
print(result)   #15


# Q2:differnace between function with parameters and without parameters
# function with parameters will accept the inputs and those inputs we can change every time.
# but without parameters we can't pass anything and values will not change dynamically
#example: function with parameter
def add(a,b):
    return a+b
print(add(1,2))
print(add(3,4))

# Example: function without parameter
def add_without_parameter():
    return 3+4
print(add_without_parameter())


#Q3 predict the output:
# def fun():
#     x=10
#     print(x)
# fun()
# print(x)

#It will throw error that x is not define after the fun() call
#because we declare and assign value inside the fun and we are trying that value outside the function. x is local to fun function only

# Q4: write a function that deos not return anything but print jay ganesh explain the default return value of such function
def say_ganesh():
    print("Jay Ganesh")

result = say_ganesh()
print(result)

# In Python, every function returns a value
# If no return is written, Python automatically returns None

#Q5: what is differnce between print(), return explain with function example
# print(): itself is function where as return is a keyword
#print is used to display the content where return is used to stop the function execution and return to the main call from function call
#print can't store any value in it  whereas return can store the value in it.
def print_return():
    print("use of print")
    return 11 #use of return

result = print_return()
print(result)


# Q6: write a program to display:
# datatype, memory address and size in bytes
import sys
a=input("Enter value: ")
print("value is: ",a)
print("value is: ",id(a))
print("value is: ",sys.getsizeof(a))

# Q7: predict the output
a=5
print(type(a))  #class 'int'
a=5.5
print(type(a))  #class 'float'
a="python"
print(type(a))  #class 'str'

#dynamically typed language

# Q9:Explain x=100 compare with c and java
# As python is dynamically typed language there no need to metion data type when we are
# assing value to variable /declartion
#but in case of java and c we need to mention the datatype when we are declaring the variable otherwise it will thorw error
# in python it will decide at run time whereas in c and java  it will decide at compile time

# Q10:
# Explain how python manages memory allocation.why does programmer not need to explicitly allocate or free memory
# Python uses automatic memory management through a private heap,
# reference counting, and garbage collection.
# Therefore, the programmer does not need to explicitly allocate or free memory,
# unlike in languages such as C.
# Python uses a private heap to store all objects.
# The programmer cannot directly access this heap.
# Python’s memory manager controls allocation and deallocation.
# Every object has a reference count (number of variables pointing to it).
# When the reference count becomes zero, memory is freed automatically.
