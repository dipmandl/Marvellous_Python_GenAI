def Display(n):
    for i in range(n, 0, -1):
        print('*' * i)


def main():
    print(Display(5))
if __name__=="__main__":
    main()