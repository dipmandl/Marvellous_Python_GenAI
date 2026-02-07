#factorial
from q1_module import add,sub,multi,div
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print(fact(5))
if __name__=="__main__":
    main()