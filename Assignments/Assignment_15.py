
# Q1 apply lambda and map function
a=lambda n:n**2
l=[12,3,4,5,6]
print(list(map(a,l)))

# Q2: lambda with filter for even number
a=lambda n:n%2==0
l=[1,2,3,4,5,6,7,8,9]
print(list(filter(a,l)))

# Q3: lambda with filter for odd number
a=lambda n:n%2!=0
l=[1,2,3,4,5,6,7,8,9]
print(list(filter(a,l)))

# Q4: lambda with reduce for sum number
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
a = lambda n1, n2: n1 + n2
result = reduce(a, l)
print(result)

# Q5: lambda with reduce for max number
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
a = lambda n1, n2: n1 if n1 > n2 else n2
print(reduce(a, l))

# Q6: lambda with reduce for min number
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
a = lambda n1, n2: n1 if n1 < n2 else n2
print(reduce(a, l))

#7 accept list of strin return string which have lenght >5
l=['hdddeded','duhdheudh','duhdheudh','sgwgs','d','dw']
a=lambda i:len(i)>5
print(list(filter(a,l)))

# Q8: lambda with filter for divisible by 3 qnd 5
a=lambda n:n%3==0 and n%5==0
l=[1,2,3,4,15,6,7,18,9]
print(list(filter(a,l)))


# Q9: lambda with reduce for product of all number
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
a = lambda n1, n2: n1 * n2
result = reduce(a, l)
print(result)

#Q10 : count of even numbers
l = [1,2,3,4,5,6,7,8,9]
a = lambda n: n % 2 == 0
print(len(list(filter(a, l))))