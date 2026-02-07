#10 even numbers:

def even(i):
    if i%2==0:
        return True
    else:
        return False

def main():
    even_cnt = 10
    evenlist = []

    for i in range(1, 100):
        if even(i):
            evenlist.append(i)
            even_cnt -= 1
        if even_cnt == 0:
            break

    print(evenlist)

if __name__=="__main__":
    main()