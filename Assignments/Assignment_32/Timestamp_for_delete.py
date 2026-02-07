import hashlib
import os
import sys
import time


def calculate_checksum(file_path):
    """Calculate MD5 checksum of a file."""
    hobj = hashlib.md5()
    with open(file_path, "rb") as fobj:
        buffer = fobj.read(1024)
        while buffer:
            hobj.update(buffer)
            buffer = fobj.read(1024)
    return hobj.hexdigest()

def remove_duplicates(directory, log_file="deleted_duplicates_with_time.log"):
    """Remove duplicate files and log deleted file names."""
    checksum_dict = {}  # key: checksum, value: first file path
    deleted_files = []
    start_time=time.time()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                checksum = calculate_checksum(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            if checksum in checksum_dict:
                # Duplicate found → delete this file
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted duplicate: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            else:
                # First occurrence → keep
                checksum_dict[checksum] = file_path

    # Log deleted files
    end_time=time.time()
    total_time=end_time-start_time
    if deleted_files:
        with open(log_file, "w") as log:
            log.write(f"Total time is required for deletion of files:  {str(total_time)}\n")
            for f in deleted_files:
                log.write(f" {f}\n")
        print(f"\nDeleted {len(deleted_files)} duplicate files. See log: {log_file}")
    else:
        print("No duplicate files found.")

def main():
    # Accept directory from command-line or user input
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory name: ")

    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    remove_duplicates(directory)

if __name__ == "__main__":
    main()
