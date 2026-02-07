import os
import shutil

def copy_all(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # creates nested dirs if needed

    for root, dirs, files in os.walk(src_dir):
        # compute the corresponding path in dest_dir
        relative_path = os.path.relpath(root, src_dir)
        dest_root = os.path.join(dest_dir, relative_path)

        os.makedirs(dest_root, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {dest_file}")

def main():
    src_dir = input("Enter Source Directory: ")
    dest_dir = input("Enter New Directory Name: ")

    if not os.path.exists(src_dir):
        print("Source directory does not exist!!")
        return

    copy_all(src_dir, dest_dir)

if __name__ == "__main__":
    print("Copying code to new directory...")
    main()
