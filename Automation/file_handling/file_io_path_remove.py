# we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling
import os
def main():
    FileName=input("Enter File Name: ")
    if os.path.exists(FileName):
        os.remove(FileName)
        print("File Deleted Successfully: ",FileName)
    else:
        print("No file Found with Name: ",FileName)


if __name__ == "__main__":
    main()

