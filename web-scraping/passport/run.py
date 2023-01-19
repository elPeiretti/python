from Prenota import Prenota
from multiprocessing import Process
import time
import datetime
import pytz

#Time (in minutes) before 00.00 to start sending petitions
MINUTES_AHEAD = 1
#Time (in seconds) before 00.00 to start sending petitions
SECONDS_AHEAD = 30

#Time (in seconds) between each "Prenota" button click, determines amount of instances needed
OFFSET = 3
#Path to file that contains the user and password
CREDENTIALS_PATH = '/home/elpeiretti/prenota.txt'

def createInstances():
    i = 0
    instances = []
    while i < MINUTES_AHEAD*60 + SECONDS_AHEAD:
        instances.append(Prenota())
        i+=OFFSET

    return instances

def getCredentials():
    creds = open(CREDENTIALS_PATH, 'r')
    usr = creds.readline()
    pwd = creds.readline()
    creds.close()
    return (usr,pwd)

if __name__ == '__main__':

    instances = createInstances()
    creds = getCredentials()
    for instance in instances:
        i = Process(target=instance.login, args=creds)
        i.start()

    #Wait until 00.00 minus MINUTES_AHEAD + SECONDS_AHEAD
    current_t = datetime.datetime.now(pytz.timezone('Europe/Rome'))
    start_t = datetime.datetime(current_t.year, current_t.month, current_t.day,23,60-MINUTES_AHEAD-1,30, tzinfo=pytz.timezone('Europe/Rome'))
    wait_t = (start_t - current_t).total_seconds()
    wait_t = 3600*(start_t.hour-current_t.hour) + 60* (start_t.minute-current_t.minute) + (start_t.second-current_t.second)
    print("Current time is:", current_t)
    print("Start time is:",start_t)
    print("Time to wait:",wait_t//3600, ":", (wait_t//60)%60,":", wait_t%60)

    time.sleep(wait_t)
    
    
    print("\n\n\n\n\n\n\nGO")
    #start clicking "Prenota" in each instance
    for instance in instances:
        Process(target=instance.pressPrenota).start()
        print("click")
        time.sleep(OFFSET)
    print("\n\nFinish")



