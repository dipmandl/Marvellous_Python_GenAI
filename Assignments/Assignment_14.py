
# Q1 apply lambda and return sqyare function
a=lambda n:n**2
n=2
print(a(n))

# Q2 apply lambda and return cube function
a=lambda n:n**3
n=2
print(a(n))

# Q3 apply lambda and return max of 2 numbers
a=lambda n1,n2:n1 if n1>n2 else n2
print(a(5,6))

# Q4 apply lambda and return min of 2 numbers
a=lambda n1,n2:n1 if n1<n2 else n2
print(a(5,6))

# Q5 apply lambda and return true if even else false
a=lambda n1:True if n1%2==0 else False
print(a(5))
print(a(4))

# Q6 apply lambda and return true if odd else false
a=lambda n1:True if n1%2!=0 else False
print(a(5))
print(a(4))

# Q7 apply lambda and return true if divisible by5
a=lambda n1:True if n1%5==0 else False
print(a(5))
print(a(4))

#Q8 accept 2 number return addition"
a=lambda n1,n2:n1+n2
print(a(5,6))
print(a(4,9))


#Q9 accept 2 number return multiplication"
a=lambda n1,n2:n1*n2
print(a(5,6))
print(a(4,9))

#Q10 accept 3 number return max from tat
a = lambda x, y, z: x if x > y and x > z else (y if y > z else z)
print(a(10, 25, 15))