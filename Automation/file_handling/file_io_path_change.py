# we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling
import os
def main():
    FileName=input("Enter File Name: ")
    if os.path.exists(FileName):
        ret=os.path.isabs(FileName)

        if ret:
            print("Absolute path: ",FileName[-1])
            fobj=open(FileName,"r")

        else:
            name=os.path.abspath(FileName)
            print("Relative path: ",FileName)
            print("Udated path is: ",name)
    else:
        print("No file Found with Name: ",FileName)


if __name__ == "__main__":
    main()
