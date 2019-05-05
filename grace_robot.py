##from gtts import gTTS
##text = "Moving left"
##tts = gTTS(text=text, lang='en', slow=False)
##tts.save("left.mp3")

import os
from gpiozero import Robot
from time import sleep
import pygame
pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=512)

robot = Robot(left=(4, 14), right=(17, 18))

##os.system("mpg123 hello.mp3")
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()

while True:
    
    os.system("mpg123 purpose.mp3")
    direction = input("Enter a direction: ")
    os.system("mpg123 "+direction+".mp3")
    if direction == "forward":
        robot.forward()
    if direction == "backward":
        robot.backward()
    if direction == "right":
        robot.right()
    if direction == "left":
        robot.left()
    if direction == "end":
        break

    sleep(3)
    robot.stop()
    

os.system("mpg123 serve.mp3")
