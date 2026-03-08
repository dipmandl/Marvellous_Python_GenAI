#commandline Input
import psutil
import sys
import os

def main():
    Border="-"*50
    print(Border)
    print("---- Marvellouse Platform Surveillance System ----")
    print(Border)

    if len(sys.argv)==2:
        if sys.argv[1]=='--h' or sys.argv[1]=='--H':
            print("This script is used to : ")
            print("1. Create a automic logs. ")
            print("2. Execute periodically. ")
            print("3. Send Email with log. ")
            print("4. Store the information about processess. ")
            print("5. Store the information about cpu. ")
            print("6. Store the information about RAM usage. ")
            print("7. Store the information about secondary storage. ")

        elif sys.argv[1]=='--u' or sys.argv[1]=='--U':
            print("use the automation script as : ")
            print("script_name.py time_interval directory_name")
            print("time_interval: the time in minutes for periodic scheduling.")
            print("directory_name: name of the directory to create auto logs.")
        else:
            print("Unable to proceed as there is no such option.")
            print("use --h or --u to get more details. ")

    #python demo.py 5 marvellous
    elif len(sys.argv)==3:
        print("Inside Project Logic.")
        print(f"Time Interval: {sys.argv[1]}")
        print(f"Directory Name:  {sys.argv[2]}")

    else:
        print("Invalid number of commandline arguments.")
        print("Unable to proceed as there is no such option.")
        print("use --h or --u to get more details. ")



    print(Border)
    print("--------- Thank You For Using Our Script ---------")
    print(Border)


if __name__=="__main__":
    main()