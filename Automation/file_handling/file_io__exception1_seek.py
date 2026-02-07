def main():
    try:
        fobj = open("hello.txt", "w")
        fobj.write("Python Automation")
        fobj = open("hello.txt", "r")
        print("File gets successfully opened")
        print("Current offset is :", fobj.tell())  #0
        fobj.seek(7)
        print("Current offset is :", fobj.tell())  #7
        data=fobj.read(10)
        print("Current offset is :", fobj.tell())  #17
        print("data is : ",data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open as there is no file with name demo.txt")
    finally:
        print("End of application")


if __name__ == "__main__":
    main()
