import pause 
from datetime import datetime
from pygame import mixer 
from time import sleep
## Schedule task to run 1x per day in the morning / early afternoon 
##  with `chron` on Linux. 
## Announce task will be executed later that day. 

def findBaseballGameTime(): 
    return "21:50"

def announceGameStart(baseballGameTime): 
    print("Got time: " + baseballGameTime)
    print("Starting announce process.")

    hourMin = baseballGameTime.split(':')

    currentDate = datetime.now() 
    gameStartDate = currentDate.replace(hour = int(hourMin[0]), minute = int(hourMin[1]), 
        second = 0, microsecond = 0)
    
    pause.until(gameStartDate)

    ## Finally, play audio file. 
    mixer.init() 
    mixer.music.load('audio.mp3')
    mixer.music.play() 

    sleep(15)


announceGameStart(findBaseballGameTime())
