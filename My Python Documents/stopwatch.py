#! python3
# stopwatch.py -- Simple stopwatch program

import time

# Display the program's instructions.

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.\nPress Ctrl+C to quit.')

# Press ENTER to begin
input()

print('Started')

# Get the first lap's start time.
starTime = time.time()
lastTime = starTime

lapNum = 1

# TODO : Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - starTime,2)
        print('Lap #%s: %s(%s)'%(lapNum,totalTime,lapTime),end='')
        lapNum += 1
        # Reset the last lap time
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl+C exception to keep its error message from displaying.
    print('\nDone...')
    