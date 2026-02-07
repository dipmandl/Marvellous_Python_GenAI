import os

def directory_scanner(directory_name="marvellous"):
    ret=os.path.exists(directory_name)

    if ret==False:
        print("There is no such directory with name: ",directory_name)
        return

    print("Contents of the Directory are: ")

    for folder_name, sub_folder_name, file_name in os.walk(directory_name):
        print("Folder Name: ", folder_name)

        for subf in sub_folder_name:
            print("Sub folder Name: ",subf)

        for fname in file_name:
            print("File name : ",fname)

def main():
    DirectoryName = input("Enter Name Of Directory: ")
    directory_scanner(DirectoryName)




if __name__ == "__main__":
    main()
