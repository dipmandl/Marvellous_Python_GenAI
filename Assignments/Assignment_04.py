# Q1: what is difference between list and tuple in terms of mutability,memory ,performance ,usecase
# A list is mutable, which means its elements can be changed after creation.
# You can add, remove, or modify elements in a list. Because of this flexibility, lists require more memory
# to store extra information needed for modification. Lists are also slightly slower
# in performance compared to tuples. Lists are commonly used when data is dynamic
# and changes frequently,
# such as storing student marks, to-do items, or collections that need updates.
#
# A tuple is immutable, meaning once it is created, its elements cannot be changed.
# Since tuples do not support modification, they use less memory than lists.
# Tuples are also faster than lists because Python can optimize access to fixed data.
# Tuples are mainly used when data should remain constant and protected, such as
# coordinates, fixed configuration values, or records that should not be modified.

# Q2: why are tuple faster than list
# in which real world scenario you would prefer tuple over list
#Tuples are faster than lists because tuples are immutable.
# Since their elements cannot be changed, Python does not need to keep extra space
# or perform additional checks for resizing or modification. Tuples have a simpler
# internal structure, which allows quicker access to elements and better optimization by Python. Lists, being mutable,
# need extra memory and processing to support adding, removing, or changing elements,
# which makes them slightly slower.

#month or days where we need to give because its fixed and no need to change again and again

# Q3 Predict the output
lst=[10,20,30]
tpt=(10,20,30)
lst[0]=100
# tpt[0]=100
#tpt[0] will raise error because its immutable and we can't change value for tuples

# Q4: Explain why strings are immutable in python what happen internally when you modufy string variable
# mmutable objects like strings can be stored in memory more efficiently.
# Python can reuse strings in multiple places (string interning) to save memory.
# Strings cannot be changed, so when you try to modify a string, Python creates a new string in
# memory and assigns it to the variable.

# Q5: Predict the output
s = "python"
print(id(s))  #2844201678000
s = s + " 3"
print(id(s))  #2844206997232
# we cna't update /modify the immutable object like string due to that it created new and assign memory location

# Q6: what is dictionary in python: explain key-value pair why key must be immutable and why duplicate keys are not allowed
# A dictionary in Python is a collection of key-value pairs. It allows you to store, access,
# and modify data using unique keys
# Key: Acts as an identifier or name. Must be unique and immutable (like string, number, tuple).
# Value: The data associated with the key. Can be of any type, mutable or immutable.
# Python dictionaries use hashing to locate keys quickly.
# Only immutable objects (like strings, numbers, tuples) have a fixed hash value
# Each key must be unique to identify a value.
# If duplicate keys were allowed, Python wouldn’t know which value to access when the key is used.
# If you define a duplicate key, Python keeps the last value and ignores previous ones

# Q7: Predict the output:
d={1:"one",1:"One",2:"Two"}
print(d)  #1:"One",2:"Two"
#because  If you define a duplicate key, Python keeps the last value and ignores previous ones

# Q8: what is range datatype in python and how its differ from list of numbers
#range is a built-in data type used to generate a sequence of numbers
# A range object is immutable and lazy, meaning it does not store all numbers in memory; it generates them on the fly when needed.
# eg range(stop)
# range(start, stop)
# range(start, stop, step)
# range is a memory-efficient, immutable sequence of numbers used for iteration. Unlike a list, it does not store all numbers in memory, making it faster and suitable for large sequences.

# Q9: Predict output
r=range(5)
print(r) # range(0, 5)
print(list(r)) #[0, 1, 2, 3, 4]

# Q10: Explain the differnce between
range(1,10)
range(1,10,2)
# both are work as range but in first call we are passing just start and end
# where as in second one we are passing step parameter as well
#so it will iterate with that value
#so in first one we will get output like
# 1,2,3,4,5,6,7,8,9
# in second on
#2,4,6,8
