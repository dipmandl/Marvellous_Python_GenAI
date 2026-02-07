import hashlib
import os
import sys
import time

def calculate_checksum(file_path):
    """Calculate MD5 checksum of a file."""
    hobj = hashlib.md5()
    try:
        with open(file_path, "rb") as fobj:
            buffer = fobj.read(1024)
            while buffer:
                hobj.update(buffer)
                buffer = fobj.read(1024)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    return hobj.hexdigest()

def remove_duplicates(directory, log_file="deleted_duplicates.log"):
    """Walk through directory, remove duplicate files, and log them with execution time."""
    checksum_dict = {}  # key: checksum, value: first file path
    deleted_files = []

    start_time = time.time()
    print(f"Scanning directory: {directory}\n")

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            if checksum is None:
                continue

            if checksum in checksum_dict:
                # Duplicate found → delete
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted duplicate: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            else:
                # Keep first occurrence
                checksum_dict[checksum] = file_path

    end_time = time.time()
    execution_time = end_time - start_time

    # Write deleted files to log with execution time
    with open(log_file, "w") as log:
        log.write("Deleted Duplicate Files Log\n")
        log.write("="*50 + "\n")
        log.write(f"Total Execution Time: {execution_time:.2f} seconds\n\n")
        for f in deleted_files:
            log.write(f"{f}\n")

    if deleted_files:
        print(f"\nDeleted {len(deleted_files)} duplicate files. See log: {log_file}")
    else:
        print("No duplicate files found.")
    print(f"Total Execution Time: {execution_time:.2f} seconds")

def main():
    # Accept directory from command-line or user input
    if len(sys.argv) >= 2:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory path: ").strip()

    # Expand ~ and normalize path
    directory = os.path.expanduser(directory)
    directory = os.path.abspath(directory)

    # Validate directory
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Directory does not exist or is invalid: {directory}")
        return

    remove_duplicates(directory)

if __name__ == "__main__":
    main()
