def CheckNum(n):
    if n%2==0:
        print(n,": Is Even")
    else:
        print(n,": Is Odd")

def main():
    CheckNum(4)
    CheckNum(5)

if __name__=="__main__":
    main()