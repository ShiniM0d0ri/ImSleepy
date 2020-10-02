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
    os.system("copy crontab.bat crontab.bak")
    FILENAME = "crontab.bat"
    f = open(FILENAME , "w")
    for i in ff:
        day = i[0]
        hour = i[1]
        duration = i[2]
        course = i[3]
        final = cron(day , hour , duration , course)
        f.write(final)
        f.write("\n")
    f.close()

def cron(day , hour , duration , course):
    path=getpath()
    #tr="python \\\""+path+"\\IamSleepy.py\\\" bg "+course+" "+duration # command to be added to task
    tr="CMD /k cd /d \\\""+path+"\\\" && python IamSleepy.py bg "+course+" "+duration
    tn=course+day+hour # task name (must be unique)
    intdur=int(duration)
    if(intdur>100):
        ET=str(int(hour)+1)+":"+str(intdur-60)
    else:
        ET=hour+":"+duration
    hour=hour+":00"
    command = f" SCHTASKS /Create /tn {tn} /tr \"{tr}\" /sc weekly /d {day} /st {hour} /et {ET} /K"
    return command

def getpath():
    path=os.getcwd()
    print(path)
    x=path.rfind("\\")
    path=path[:x]
    return path
    
main()
