##This program poses 10 multiplication problems to the user and only accepts the correct answers.

# First we'll import pyinputplus,random and time modules

import pyinputplus as pyip
import random,time

# We'll track of how many questions the program asks and how many correct answer the user gives

numberOfQuestions = 10
correctAnswers = 0

# For loop wil repeatedly pose a random multiplication problem 10 times.

for questionNumber in range(numberOfQuestions):
    # Inside the for loop the program will pick two single digit numbers to multiply.
    # We'll use these numbers to create a #Q:N x N = prompt for the user, where Q is the question number (1 to 10) and N are the two numbers to multiply
    #Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s :%s x %s ='%(questionNumber,num1,num2)
    # The pyip.inputStr() will handle most of the features of this program.
    # The argument we pass for allowRegexes is a list with the regex string '^%s$'
    # where %s is replaced with the correct answer
    # blocklistRegexes is a list with ('.*','Incorrect!') first string in he tuple is a regex that matches every possible string.Thereforeif he user response doesn't match the correct answer program will reject any other answer they provide.In that case the 'Incorrect!' string is displayed.
    # Additionally passing 8 for timeout and 3 for limit will ensure that user has only 8 seconds and 3 tries to provide a correct answer
    try:
        # Right answers are handled by allowRegexes.
        # Wrong asnwers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1 * num2)],
                    blockRegexes=[('.*','Incorrect!')],
                    timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let user see the result.
    print('Score: %s/%s'%(correctAnswers,numberOfQuestions))