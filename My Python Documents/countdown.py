#! python3
# countdown.py -- A simple countdown script.

import subprocess,time,os

os.chdir('C:\\Users\\devil\\Desktop\\Python Beginners Code and Basics\\Automate the boring staff with Python\\Files used in the book\\Automate_the_Boring_Stuff_2e_onlinematerials\\automate_online-materials')

timeLeft = 60
while timeLeft > 0:
    # use end='' to skip display
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1 

# TODO : At the end of the countdown, play a sound file.

subprocess.Popen(['start','alarm.wav'],shell=True)
