import os.path
import sys
import time
import schedule

def DirectoryScanner(DirName="Marvellous"):
    Border = "-" * 50
    print(Border)
    timestmap=time.ctime()

    timestmap=timestmap.replace(":","_")
    timestmap = timestmap.replace(" ", "_")
    logfile_name="Marvellous_%s.log"%(timestmap)

    fobj=open(logfile_name,"w")
    fobj.write(Border+"\n")
    fobj.write("This  Is A Log File Created By Marvellous Automation\n")
    fobj.write("This  Is a Directory\n")
    fobj.write(Border+"\n")
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

    fobj.write("\n-------------- Automation Report ----------------\n")
    # fobj.write("Total Files Scanned : "+str(file_cnt)+"\n")
    fobj.write(f"Total Files Scanned : {file_cnt} \n")
    fobj.write(f"Total Empty File Found : {empty_file_cnt} \n")
    fobj.write(f"This File Is Created At : {timestmap} \n")
    fobj.write(Border+"\n")




def main():
    Border="-"*50
    print(Border)
    print("---------Marvellous Dircetory Automation Start----------")
    print(Border)

    if len(sys.argv)!=2:
        print("Invalid Number of Arguments!!")
        print("Please specify the name of directory")
        return
    # DirectoryScanner(sys.argv[1])
    schedule.every(1).minute.do(DirectoryScanner)
    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("---------Marvellous Dircetory Automation END----------")
    print(Border)

if __name__=="__main__":
    main()
