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

def FindDuplicate(DirectoryName="marvellous"):
    ret=os.path.exists(DirectoryName)
    if ret==False:
        print("There Is No such Directory.")
        return
    ret=os.path.isdir(DirectoryName)
    if ret==False:
        print("It is not directory")
        return

    Duplicate={}
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            CheckSum=calculate_checksum(fname)
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum]=[fname]

    return Duplicate

def DisplayResult(MyDict):
    Result=list(filter(lambda x:(len(x)>1),MyDict.values()))
    Count=0

    for value in Result:
        for sub_value in value:
            Count=Count+1
            print(sub_value)
        print("Value of Count is : ",Count)
        Count=0


def DeleteDuplicate(Path="marvellous"):
    MyDict=FindDuplicate(Path)
    Result = list(filter(lambda x: (len(x) > 1), MyDict.values()))
    # Count = 0
    cnt=0
    for value in Result:
        Count = 0
        for sub_value in value:
            Count = Count + 1
            if Count>1:
                print("Deleted File: ",sub_value)
                os.remove(sub_value)
                cnt=cnt+1


    print("Total Deleted File: ",cnt)
def main():

    DeleteDuplicate()

if __name__=="__main__":
    main()



