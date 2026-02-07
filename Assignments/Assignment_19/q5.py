from functools import reduce
# Lambda to check prime
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
sq=lambda i:i*2
max_func = lambda a, b: a if a > b else b

l=[23,2,3,4,656,12,433]
print(list(filter(is_prime,l)))
print(list(map(sq,l)))
print(reduce(max_func, l))

