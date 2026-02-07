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
    file_cnt=0
    empty_file_cnt=0
    for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            file_cnt = file_cnt + 1
            fname=os.path.join(FolderName,fname)
            if os.path.getsize(fname)==0: #Empty file
                empty_file_cnt=empty_file_cnt+1
                os.remove(fname)
    print()
    print("-------------- Automation Report ----------------")
    print("Total Files Scanned : ",file_cnt)
    print("Total Empty File Found : ",empty_file_cnt)
    print()




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

    print(Border)
    print("---------Marvellous Dircetory Automation----------")
    print(Border)

if __name__=="__main__":
    main()
