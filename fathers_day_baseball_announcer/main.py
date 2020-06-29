import pause 
from datetime import datetime
from pygame import mixer 
from time import sleep

## Schedule task to run 1x per day in the morning / early afternoon 
##  with `cron` on Linux. 
## Announce task will be executed later that day. 

def findBaseballGameTime(): 
    return "21:50"

def announceGameStart(baseballGameTime): 
    print("Starting announce process.")
    print("Got time: " + baseballGameTime)

    colonSepDate = baseballGameTime.split(':')

    currentDate = datetime.now() 
    gameStartDate = currentDate.replace(year = int(colonSepDate[2]), month = int(colonSepDate[0]), day = int(colonSepDate[1]),
        hour = int(colonSepDate[3]), minute = int(colonSepDate[4]), 
        second = 0, microsecond = 0)
    
    pause.until(gameStartDate)

    ## Finally, play audio file. 
    print("Announcing...")
    mixer.init() 
    mixer.music.load('audio.mp3')
    mixer.music.play() 

    sleep(15)

    print("Finished.")



gameTimes = ["06:28:2020:19:32"]

for time in gameTimes: 
    announceGameStart(time)
