def CheckNum(n):
    if n>0:
        print(n,": Is Positive")
    elif n<0:
        print(n,": Is Negative")
    else:
        print("number is zero")

def main():
    CheckNum(4)
    CheckNum(-5)
    CheckNum(0)



if __name__=="__main__":
    main()