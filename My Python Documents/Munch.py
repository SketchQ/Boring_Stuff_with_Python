'''
Munch App MVP
v0.1
By Erim Serdönmez
THe purpose of Munch is to produce a dinner from favourite dishes, and produce
a shopping list of ingredients if required.
'''
#----- Imports-----------

from random import choice


# -----A. Functions------

# A1. Choose dishes

def chooseDishes(days):   
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu... ")
    print()
    for i in myMenu:
        print(myMenu.index(i) +1, i)
    print()
    print("Out of all these dishes, my favorite has to be... " + choice(myMenu))
    '''
    1. Choose a random dish from foodWeLike - Done!
    2. Make sure the dish hasn't been chosen. If not, add to myMenu - Done!
    3. Repeat the code until we have required number of dishes in myMenu -Done!
    '''
# A2. Build shopping list

def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(Pizza)
    if "Burger" in myMenu:
        myShoppingList.append(Burger)
    if "Pasta" in myMenu:
        myShoppingList.append(Pasta)
    if "Meatball" in myMenu:
        myShoppingList.append(Meatball)
    if "Chicken" in myMenu:
        myShoppingList.append(Chicken)
    if "Fish" in myMenu:
        myShoppingList.append(Fish)
    if "Patato" in myMenu:
        myShoppingList.append(Patato)
    print()
    for i in myShoppingList:
        for v in i:
            print(v)
    print()
    print("Voilaa!!!! Bon Apetit!")
# A3. Goodbye Function

def goodbye():
    print()
    print("You got it! Bye for now :)")
    

#------ B. Lists---------


foodWeLike = ["Pizza", "Burger", "Pasta", "Meatball","Chicken", "Fish", "Patato" ]

Pizza = ["Pizza Base", "Tomato Sauce", "Cheese", "Pepperoni", "Chilis"]
Burger = ["Bread", "Meat", "Cabbage", "Pickles", "Ketchup"]
Pasta = ["Pasta", "Tomato paste", "Olive oil", "Cheese"]
Meatball = ["Meatballs", "Salad"]
Chicken = ["Chicken", "Patato", "Tomato Paste", "Olive Oil",]
Fish = ["Fish", "Wine"]
Patato = ["Patato", "Tomato Paste", "Olive Oil"]

myMenu = []

#1. How many days to plan? (Django)

print("Hello, I'M Munch! I'll help you to plan your dinner menu...")

answer = input("How many days would you like me to plan? ")

print("OK, I'm going to plan " + answer + " dinner(s) from your favourite meals list")

#2. Choose dishes

chooseDishes(answer)


#3. Build shopping list?
while True:
    answer = input("Would you like a shopping list for this menu? Enter 'y' or 'n'...")
    if answer in ('y', 'Y', 'n', 'N'):
        break
        print("Oopss!, I didn't catch that one. Please press y or n")
if answer in ('y', 'Y'):
    buildShoppingList()
else:
    goodbye()
   
        

