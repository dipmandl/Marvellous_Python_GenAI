import os

import os


def main():
    DirectoryName = input("Enter Name Of Directory: ")


    for folder_name, sub_folder_name, file_name in os.walk(DirectoryName):
        print("Folder Name: ", folder_name)

        for subf in sub_folder_name:
            print("Sub folder Name: ",subf)

        for fname in file_name:
            print("File name : ",fname)



if __name__ == "__main__":
    main()
