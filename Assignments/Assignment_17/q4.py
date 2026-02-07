#addition of factors:
def sum_of_factors(n):
    factors = []
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            total += i
    return factors, total

def main():
    num=88
    factors, total = sum_of_factors(num)
    print(f"Factors of {num} are: {factors}")
    print(f"Sum of factors: {total}")
if __name__=="__main__":
    main()