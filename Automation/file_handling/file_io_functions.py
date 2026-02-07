# we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling
import os
def main():
    FileName=input("Enter File Name: ")
    if os.path.exists(FileName):
        fobj=open(FileName,"r")
        print(fobj.name)
        print(fobj.mode)
        print(fobj.closed)
        fobj.close()
        print(fobj.closed)

    else:
        print("No file Found with Name: ",FileName)


if __name__ == "__main__":
    main()

