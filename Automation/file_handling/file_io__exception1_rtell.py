
# we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling

def main():
    try:
        fobj = open("hello.txt", "r")
        print("File gets successfully opened")
        print("Current offset is :",fobj.tell())
        data=fobj.read(6)
        print("Current offset is :", fobj.tell())
        print("data is : ",data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open as there is no file with name demo.txt")
    finally:
        print("End of application")


if __name__ == "__main__":
    main()
