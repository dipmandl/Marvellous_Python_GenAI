#creating log file
import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-" * 50
    ret=os.path.exists(FolderName)
    if ret:
        ret=os.path.isdir(FolderName)
        if ret==False:
            print("Unable to process")
            return


    else:
        os.mkdir(FolderName)
        print(f"Directory : {FolderName} is Created Successfully")

    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name=os.path.join(FolderName,f"Marvellous_{timestamp}.log")
    # print(file_name)
    fobj=open(file_name,"w")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellouse Platform Surveillance System ----\n")
    fobj.write("Log created at: "+time.ctime()+"\n")
    fobj.write(Border+"\n\n\n")
    fobj.write("-------------System Report--------------")
    fobj.write(Border + "\n")

    fobj.write(f"CPU Usage: {psutil.cpu_percent()}%\n")
    fobj.write(Border + "\n")

    mem = psutil.virtual_memory()
    fobj.write(f"Ram Usage: {mem.percent}%\n")
    fobj.write(Border + "\n")

    fobj.write("Disk Usage Report: \n")
    fobj.write(Border + "\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write(f"{part.mountpoint}  -> used {usage.percent}%\n")
        except:
            pass
    fobj.write(Border + "\n")
    net=psutil.net_io_counters()
    fobj.write(f"Network Usage Report: \n")
    fobj.write(Border + "\n")
    fobj.write(f"Sent : {((net.bytes_sent)/1024*1024)} MB \n")
    fobj.write(f"Received : {((net.bytes_recv)/1024*1024)} MB \n")

    fobj.write(Border + "\n")
    #Process Log
    fobj.write("--------- Process Log ---------\n")
    data=ProcessScan()
    for i in data:
        fobj.write("PID : %s\n" %i.get("pid"))
        fobj.write("Name : %s\n" %i.get("name"))
        fobj.write("Username : %s\n" %i.get("username"))
        fobj.write("Status : %s\n" %i.get("status"))
        fobj.write("Start time : %s\n" %i.get("create_time"))
        fobj.write("CPU : %s\n" %i.get("cpu_percent"))
        fobj.write("Memory : %s\n" %i.get("memory_percent"))
        fobj.write(Border + "\n")


    fobj.write(Border+"\n")
    fobj.write("--------- End Of Log File ---------\n")
    fobj.write(Border+"\n")

def ProcessScan():
    print("Process Scan Report")
    information=[]

    #Warm up for CPU percent
    for p in psutil.process_iter():
        try:
            p.cpu_percent()
        except:
            pass
    time.sleep(0.2)
    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["pid","name","status","username","create_time","cpu_percent","memory_percent"])
            #convert create_time
            try:
                info["create_time"]=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime((info["create_time"])))
            except:
                info["create_time"]="NA"
            info["cpu_percent"]=proc.cpu_percent(None)
            info["memory_percent"]=proc.memory_percent()
            information.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return information


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
        # apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Surveillance System Started Succesfully")
        print("Direcctory Created with name: ",sys.argv[2])
        print("Time Interval In Minutes",sys.argv[1])
        print("Press Ctrl + C to stop execution.")
        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of commandline arguments.")
        print("Unable to proceed as there is no such option.")
        print("use --h or --u to get more details. ")



    print(Border)
    print("--------- Thank You For Using Our Script ---------")
    print(Border)


if __name__=="__main__":
    main()