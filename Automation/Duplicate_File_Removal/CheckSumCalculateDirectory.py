import hashlib
import os
#hashlib is os dependent
#need to check the how we can delete old file.
def calculate_checksum(FileName):
    fobj=open(FileName,"rb")
    hobj=hashlib.md5()

    Buffer=fobj.read(1024)
    while len(Buffer)>0:
        hobj.update(Buffer)
        Buffer=fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName="marvellous"):
    ret=os.path.exists(DirectoryName)
    if ret==False:
        print("There Is No such Directory.")
        return
    ret=os.path.isdir(DirectoryName)
    if ret==False:
        print("It is not directory")
        return

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            CheckSum=calculate_checksum(fname)
            print(f"File Name : {fname} checksum is : {CheckSum}")

def main():

    DirectoryWatcher()

if __name__=="__main__":
    main()



