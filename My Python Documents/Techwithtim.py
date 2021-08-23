### Playing Around with the python
### Erim Serdönmez
import json

'''-------FUNCTIONS-----'''
def get_age(answer):
    if int(answer) == 17:  
        print("\nYou can't get married.But next year you will be ")
    elif int(answer) > 18:
        print("\nGratz, you can get married. ")
    else:
        print("\nSorry you are too young. ")        


print("Hello! Welcome to my freewriting program. \n Please press any key to continue: ")
i = input()
username = input("To continue you must have an username but don't worry I can save your username for future use. \n Would you like me to save your username? ...\npress 'y' or 'n' to continue...")

file_name = "username.json"
email_file = "email_file.json"

if username == "y":
    try:
        with open(file_name) as file_object:
            username1 = json.load(file_object)
    except FileNotFoundError:
        username1 = input("\n Please write your username? ")
        with open(file_name, "a") as file_object:
            json.dump(username1,file_object)
            print("\nThank you for your coorperation. ")
    else:
        print("Welcome back " + username1 +" .")
if username == "n":
    username1 = input("\nOk no worries, Please write your username. ")
    print("Thank you for signing up " + username1)

print("\n ----------------------------------\n")

prompt = input("Please write your email adress: \n")

while prompt.find("@") == -1:
    print("Please us '@' in your email. ")
    prompt = input("\nWhat is your email adress.")
else:
    print("Thank you.\n If you like us to store your email adress press 'y'... \n if not, press any other key: ")        
    email = input()
if email == 'y':
    with open(email_file, "w") as file_object:
        json.dump(prompt,file_object)
        print("your email was saved. ")
if email != 'y':
    print("\nThank you, your email will not be saved. ")   

with open(email_file) as file_object:
    email=json.load(file_object)

prompt = input("Please enter your password: \n")


while int(len(prompt)) < 5:
    print("Your pasword must be longer than 5 ")
    prompt = input("Please enter your password: \n")
else:
    print("Thank you. ")


print("Enter 'q' to exit the program. ")
'''
while True:
    answer = input("\nPlease write your age to find out if you are eligiable to marry?  ")
    if answer == 'q':
        break
    get_age(answer)
'''    
    
