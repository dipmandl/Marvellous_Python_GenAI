# we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling
import os
def main():
    FileName=input("Enter File Name: ")
    ret=os.path.exists(FileName)
    if ret:
        print("File Found!!, Opening the file in Read Mode: ",FileName)
        fobj=open(FileName,"r")
    else:
        print("There no file with Name: ",FileName)

if __name__ == "__main__":
    main()
