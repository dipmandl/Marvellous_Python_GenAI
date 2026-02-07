import hashlib

#hashlib is os dependent

def calculate_checksum(FileName):
    fobj=open(FileName,"rb")
    hobj=hashlib.md5()

    Buffer=fobj.read(1024)
    while len(Buffer)>0:
        hobj.update(Buffer)
        Buffer=fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def main():
    checksum=calculate_checksum("Demo.txt")
    print(f"Checksum is: {checksum}")

if __name__=="__main__":
    main()



