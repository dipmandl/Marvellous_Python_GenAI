def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # get last digit
        n = n // 10      # remove last digit
    return total
def main():
    print(sum_of_digits(868627665))
if __name__=="__main__":
    main()