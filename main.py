# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
import pygame
from datetime import datetime,timedelta
def water():
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play(0)
    f = open("water.txt","a")
    str = input("Did you drank the water??\n")
    if(str=="drank"):
        f.write(f"{datetime.datetime.now()}  -   Drank")
        f.close()
        pygame.mixer.music.stop()
def eyes():
    currenttime = datetime.datetime.now().time()
    playtime = datetime.timedelta(minutes=30,seconds=0)
    pygame.mixer.music.load('eye.mp3')
    pygame.mixer.music.play(0)
    flag = input("Did you finish the eye exercise?? (Yes/No)")
    if (flag == "Yes"):
        pygame.mixer.music.stop()
        f = open("eye.txt","a")
        f.write(f"{currenttime} - Eye exercise done")
        f.close()
def exercise():
    currenttime = datetime.datetime.now().time()
    playtime = datetime.timedelta(minutes=30, seconds=0)
    pygame.mixer.music.load('exercise.mp3')
    pygame.mixer.music.play(0)
    flag = input("Did you finish the exercise?? (Yes/No)")
    if (flag == "Yes"):
        pygame.mixer.music.stop()
        f = open("exercise.txt", "a")
        f.write(f"{currenttime} - exercise done")
        f.close()
if __name__ == '__main__':
        starttime = datetime.now()
        watertime = starttime+timedelta(minutes=15)
        eyetime = starttime+timedelta(minutes=30)
        extime = starttime+timedelta(minutes=45)
        while True:
            if(watertime==datetime.now()):
                water()
                watertime = datetime.now() + timedelta(minutes=15)
            if(eyetime==datetime.now()):
                eyes()
                eyetime = datetime.now() + timedelta(minutes=30)
            if(extime==datetime.now()):
                exercise()
                extime = datetime.now() + timedelta(minutes=45)







