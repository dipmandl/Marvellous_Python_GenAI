#Check the file exist in current directory
import os
filename=input("Enter File Name you want to check: ")
if os.path.exists(filename.lower()) or os.path.exists(filename.upper()):
    print("File Exitst in Current Directory")
else:
    print("File Not found in Current Directory")

#display content of files:
data=open(filename,"r")
print(data.read())