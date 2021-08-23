import random

print("Welcome to the NumberGuesserr")
name = input("What is your name? ")

secretNumber = random.randint(1,20)

print("Welcome to my game " + name + " I'm thinking a number between 1 and 20...\n Please write your answer...")

try:
    for i in range(1,7):
        guessedNumber = int(input())
        if guessedNumber < secretNumber:
            print(" Your Guess is too low")
        elif guessedNumber > secretNumber:
            print(" Your Guess is too high ")
        else:
            break
    if guessedNumber == secretNumber:
        print(" Gratz!! You've guessed it correct! " + name + "\n It took you " + str(i) + " times.")
    else:
        print(" I'm sorry you are out of lives...\n The secret number was: " + str(secretNumber))
except ValueError:
    print(" You have to type a number not letters.")