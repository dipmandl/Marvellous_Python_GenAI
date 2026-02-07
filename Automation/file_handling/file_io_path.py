# we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling
import os
def main():
    FileName=input("Enter File Name: ")
    ret=os.path.isabs(FileName)
    name=os.path.abspath(FileName)
    if ret:
        print("Absolute path Is : ",FileName)
        fobj=open(FileName,"r")

    else:
        print("Relative path: ",FileName)


if __name__ == "__main__":
    main()
