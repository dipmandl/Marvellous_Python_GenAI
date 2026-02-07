def Display(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()  # move to next line


def main():
    Display(5)
if __name__=="__main__":
    main()