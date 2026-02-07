import hashlib
import os
import sys

def calculate_checksum(file_path):
    """Calculate MD5 checksum of a file."""
    hobj = hashlib.md5()
    with open(file_path, "rb") as fobj:
        buffer = fobj.read(1024)
        while buffer:
            hobj.update(buffer)
            buffer = fobj.read(1024)
    return hobj.hexdigest()

def checksum_directory(directory):
    """Walk through directory and calculate checksum for all files."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            print(f"{file_path} -> {checksum}")

def main():
    # Accept directory from command-line or user input
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory name: ")

    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    checksum_directory(directory)

if __name__ == "__main__":
    main()
