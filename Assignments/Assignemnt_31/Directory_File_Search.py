import sys
import os

def scan_files(directory_name="Marvellous",file_extensio='txt'):
    for folder_name,sub_folder_name,file_name in os.walk(directory_name):
        for file in file_name:
            if file.endswith(file_extensio):
                print(file)


def main():
    directory_name=''
    file_extension=''
    if len(sys.argv)!=3:
        directory_name=input("Enter Directory Name: ")
        file_extension=input("Enter File Extension: ")
    else:
        directory_name=sys.argv[1]
        file_extension=sys.argv[2]

    if not os.path.exists(directory_name):
        print("Directory does not exist!!")
        return
    scan_files(directory_name,file_extension)

if __name__=="__main__":
    print("Searching file with extension in directory!!")
    main()