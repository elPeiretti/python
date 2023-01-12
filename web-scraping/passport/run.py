from Prenota import Prenota
from multiprocessing import Process
import time
import datetime
import pytz

#Time (in minutes) before 00.00 to start sending petitions
TIME_AHEAD = 1
#Time (in seconds) between each "Prenota" button click, determines amount of instances needed
OFFSET = 2
#Path to file that contains the user and password
CREDENTIALS_PATH = '/home/elpeiretti/prenota.txt'

def createInstances():
    i = 0
    instances = []
    while i < TIME_AHEAD*60 + 20:
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

    #Wait until 00.00 minus TIME_AHEAD
    current_t = datetime.datetime.now(pytz.timezone('Europe/Rome'))
    start_t = datetime.datetime(current_t.year, current_t.month, current_t.day,23,60-TIME_AHEAD,0, tzinfo=pytz.timezone('Europe/Rome'))
    print((start_t - current_t).total_seconds())
    time.sleep((start_t - current_t).total_seconds())
    
    
    print("\n\n\n\n\n\n\nGO")
    #start clicking "Prenota" in each instance
    for instance in instances:
        Process(target=instance.pressPrenota).start()
        #instance.pressPrenota()
        print("click")
        time.sleep(OFFSET)
    print("\n\nFinish")



