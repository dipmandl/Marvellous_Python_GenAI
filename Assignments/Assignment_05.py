# Q1 what are bytes in python
# bytes is a built-in data type that represents a sequence of 8-bit values, i.e., integers from 0 to 255. Bytes are mainly used to work with
# binary data rather than human-readable text
# Bytes in Python are immutable to ensure safety, data integrity, hashability, and performance.
# Any modification creates a new bytes object instead of changing the original.

# Q2: Predict the output and explain why number are converte internally
b=bytes([65,66,67])
print(b)  #ABC


# When you create a bytes object from integers, Python stores the numbers internally (0–255), but prints them as ASCII characters if possible.
# This conversion is only for readability, the underlying data remains numeric.

# Q3: what is difference between bytes and bytesarray mentioned mutability and usecase

# Mutability
# bytes :immutable
# Once created, you cannot change the contents.
# Any modification creates a new bytes object.
# bytearray :mutable
# You can modify the contents after creation (change, add, or remove bytes).
# Bytes (immutable):
# When working with fixed binary data that should not change.
# Examples: reading binary files, network packets, cryptographic keys.
# Bytearray (mutable):
# When you need to modify binary data after creation.
# Examples: editing images/audio in memory, building a network message dynamically, manipulating files.


# Q4: predict output and tell why ?
b=bytearray([65,66,67])
b[0]=97
print(b)  #aBC
#this is allowed because bytearray is mutable


# Q5 what is None in python and its same 0,False or empty string python
#None is a special constant that represents the absence of a value or nothing. It is a built-in data type (NoneType) and is often used to indicate that a variable has no value yet or a function does not return
#its not same as 0,False, or empty string

# Q6:
x=None
print(type(x)) #<class 'NoneType'>
print(x==False)  #False
#because None is a special constant that represents the absence of a value or nothing it will not tell boolean

# Q8: what is set in python
# a set is a collection of unique elements. Sets are unordered, mutable, and do not allow duplicate values
# Unordered – Elements have no specific order; you cannot access items by index.
# Mutable – You can add or remove elements.
# No duplicates – Every element must be unique.
# Iterable – You can loop through all elements in a set

#Q9 : predict the output why few values are missing.
s={10,20,30,40,20}
print(s)    #{10,20,30,40}
# a set is a collection of unique elements it removing the duplicate entry

# Q10:
#Dynamic typing means that in Python, you do not need to declare the type of a variable when you create it. Python automatically determines the type at runtime based on the value assigned.
a = 10        # x is an integer
print(type(a))  # Output: <class 'int'>

a = "Hello"   # Now x is a string
print(type(a))  # Output: <class 'str'>

a = 3.14      # Now x is a float
print(type(a))  # Output: <class 'float'>




