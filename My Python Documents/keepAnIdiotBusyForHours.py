## We will write a program that does the following:
    # 1.Asks the user if they'd like to know how to keep an idiot busy for hours.
    # 2.If the user answer no,quit
    # 3.If the user answers yes, go to step 1.

import pyinputplus as pyip

## Ask the user's input

while True:
    print('Want to know how to keep an idiot busy for hours?')
    answer = pyip.inputYesNo()
    if answer == 'yes':
        continue
    elif answer == 'no':
        print('Thank you')
        break