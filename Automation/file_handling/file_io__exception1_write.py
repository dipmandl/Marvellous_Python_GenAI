#we have open(),close(),read(),write(),remove(),tell(),seek() functions for file handling

def main():
    try:
            open("hello.txt","w")
            print("File gets successfully opened")
    except FileNotFoundError:
        print("Unable to open as there is no file with name demo.txt")
    finally:
        print("End of application")

if __name__=="__main__":
    main()
