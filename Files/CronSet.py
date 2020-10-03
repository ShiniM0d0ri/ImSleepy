import os
import string


def main():
    final_list = []
    f = open("TimeTable.txt")
    lines = f.readlines()
    for i in lines:
        stripped = i.strip()
        ll = stripped.split()
        final_list.append(ll)
    final_list.pop(0)
    setCron(final_list)
    f.close()

def setCron(ff):
    # Just to be safe
    while True:
        backg=input("Type bg and press enter if you want to run in background mode: ")
        if backg=="bg" or backg=="":
            break
        else:
            print("Not an valid input !!")
    os.system("copy crontab.bat crontab.bak")
    FILENAME = "crontab.bat"
    f = open(FILENAME , "w")
    f.write("@echo OFF \n")
    for i in ff:
        day = i[0]
        hour = i[1]
        duration = i[2]
        course = i[3]
        final = cron(day , hour , duration , course, backg)
        f.write(final)
        f.write("\n")
    f.write("pause")
    f.close()

def cron(day , hour , duration , course,backg):
    path=getpath()
    tr="CMD /k cd /d \\\""+path+"\\\" && python IamSleepy.py "+backg+" "+course+" "+duration
    tn=course+day+hour # task name (must be unique)
    intdur=int(duration)
    if(intdur>100):
        ET=str(int(hour)+1)+":"+str(intdur-60)
    else:
        ET=hour+":"+duration
    hour=hour+":00"
    command = f"SCHTASKS /Create /tn {tn} /tr \"{tr}\" /sc weekly /d {day} /st {hour} /et {ET} /K"
    return command

def getpath():
    path=os.getcwd()
    print(path)
    x=path.rfind("\\")
    path=path[:x]
    return path
    
main()
