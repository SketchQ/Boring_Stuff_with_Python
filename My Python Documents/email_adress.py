import random
answer = (random.randrange(0,50))
print(answer)

prompt = input("Please select a random number between 0-50\n")


while int(prompt) != int(answer):
    while int(prompt) == int(answer):
        print("Correct!!! you got it.")
        break
    if int(prompt) > int(answer):
        print("Too high, try to go lower.")
        prompt = input("Please select a random number between 0-50\n")
    if int(prompt) < int(answer):
        print("Too low try to higher. ")
        prompt = input("Please select a random number between 0-50\n")




