#factorial
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return str(n)+" Is not prime number"
    return str(n)+" Is prime number"

def main():
    print(is_prime(5))
if __name__=="__main__":
    main()