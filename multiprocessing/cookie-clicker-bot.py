import multiprocessing
import time
import keyboard
from python_imagesearch.imagesearch import imagesearch
import pyautogui

count = 0
pyautogui.PAUSE=0.01

def bot():

    while(1):
        pyautogui.click(293,446)

def startProcess(t):
    p=multiprocessing.Process(target=t)
    p.start()
    return p

def goldenCookieFinder():
    global count
    proc = startProcess(bot)
    proc.daemon=True
    while(1):
        pos = imagesearch('C:/Users/Tomas/Desktop/goldCookie.png') 
        if pos[0] != -1:
            proc.terminate()
            proc.join()
            posx=pos[0]
            posy=pos[1]
            pyautogui.moveTo(posx+10, posy+10)
            pyautogui.click()
            count+=1

            proc = startProcess()
            proc.daemon=True
        time.sleep(10)




if __name__ == "__main__":
    finder = startProcess(goldenCookieFinder)
    
    while(not keyboard.is_pressed("f6")):
        pass
    
    finder.terminate()
    finder.join()

    print(count)

