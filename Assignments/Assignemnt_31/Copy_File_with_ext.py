import os
import shutil

def copy_filtered(src_dir, dest_dir, file_ext):
    # Ensure extension starts with a dot
    if not file_ext.startswith("."):
        file_ext = "." + file_ext.lstrip(".")

    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")

    # Walk through source directory recursively
    for root, dirs, files in os.walk(src_dir):
        # Compute corresponding path in destination
        relative_path = os.path.relpath(root, src_dir)
        dest_root = os.path.join(dest_dir, relative_path)
        os.makedirs(dest_root, exist_ok=True)

        # Copy only files matching the extension
        for file in files:
            if file.lower().endswith(file_ext.lower()):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_root, file)
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {dest_file}")

def main():
    src_dir = input("Enter Source Directory: ")
    dest_dir = input("Enter New Directory Name: ")
    file_ext = input("Enter File Extension to Copy (e.g., txt): ")

    if not os.path.exists(src_dir):
        print("Source directory does not exist!")
        return

    copy_filtered(src_dir, dest_dir, file_ext)
    print("\nCopying complete!")

if __name__ == "__main__":
    main()
