filtr=lambda i:i>=70
mp=lambda i:i+10
rd = lambda n1, n2: n1 + n2

lst=[1,2,3,4,5,6,7,8,9,87,563,768]
#print grater than 70
print(list(filter(filtr,lst)))

#print add 10 to each element
print(list(map(mp,lst)))

#sum of all numbers
from functools import reduce
print(reduce(rd,lst))