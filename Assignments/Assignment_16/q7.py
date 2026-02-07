def CheckNum(n):
    if n%5==0:
        return True
    else:
        return False

def main():
    ans=CheckNum(4)
    print(ans)
    ans=CheckNum(5)
    print(ans)

if __name__=="__main__":
    main()