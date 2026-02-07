import os.path
import sys

def DirectoryScanner(DirName="Marvellous"):
    Ret=False
    Ret=os.path.exists(DirName)
    if Ret==False:
        print("There is no such directory")
        return
    Ret=os.path.isdir(DirName)
    if Ret==False:
        print("Its not a directory")
        return

    for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            print("File Name: ",fname)
            print("Size of File: ",os.path.getsize(fname))  # we will get here path issue solution provided in next file



def main():
    Border="-"*50
    print(Border)
    print("---------Marvellous Dircetory Automation----------")
    print(Border)

    if len(sys.argv)!=2:
        print("Invalid Number of Arguments!!")
        print("Please specify the name of directory")
        return
    DirectoryScanner(sys.argv[1])

if __name__=="__main__":
    main()
