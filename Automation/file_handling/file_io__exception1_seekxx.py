#seek(offset,whence)
#seek(kuthe,kuthun)
#kuthun: 0/1/2
#0: starting
#1: Current
#2: End
def main():
    try:
        fobj = open("hello.txt", "w")
        fobj.write("Python Automation")
        fobj = open("hello.txt", "rb")
        print("File gets successfully opened")
        print("Current offset is :", fobj.tell())  #0
        fobj.seek(-8,2)
        print("Current offset is :", fobj.tell())  #11

        data=fobj.read(8)
        print("data is : ", data)
        print("Current offset is :", fobj.tell())  #17

        fobj.close()

    except FileNotFoundError:
        print("Unable to open as there is no file with name demo.txt")
    finally:
        print("End of application")


if __name__ == "__main__":
    main()
