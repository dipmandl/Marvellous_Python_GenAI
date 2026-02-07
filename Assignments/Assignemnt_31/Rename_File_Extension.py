import sys
import os


def rename_file(directory_name, old_ext, new_ext):
    old_ext = "." + old_ext.lstrip(".")
    new_ext = "." + new_ext.lstrip(".")

    for folder_name, sub_folder_name, file_list in os.walk(directory_name):
        for file in file_list:
            name, ext = os.path.splitext(file)

            # ONLY replace old extension
            if ext.lower() == old_ext.lower():
                old_path = os.path.join(folder_name, file)
                new_path = os.path.join(folder_name, name + new_ext)

                if os.path.exists(new_path):
                    print(f"Skipped (already exists): {new_path}")
                    continue

                os.rename(old_path, new_path)
                print(f"Renamed: {file} -> {name + new_ext}")




def main():
    directory_name=''
    old_file_extension=''
    new_file_extension=''
    if len(sys.argv)!=4:
        directory_name=input("Enter Directory Name: ")
        old_file_extension=input("Enter File Extension to Replace: ")
        new_file_extension=input("Enter New File Extension: ")
    else:
        directory_name=sys.argv[1]
        old_file_extension=sys.argv[2]
        new_file_extension=sys.argv[3]

    if not os.path.exists(directory_name):
        print("Directory does not exist!!")
        return
    rename_file(directory_name,old_file_extension,new_file_extension
               )

if __name__=="__main__":
    print("Searching file with extension in directory!!")
    main()