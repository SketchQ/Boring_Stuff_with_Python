'''
name="User Welcome to my program"
quote=("It's better to burn away then fadeaway...")
numbers = ("1,\n2,\n3,\n4,\n5..." )
start =("Let's get started with Python..")
first_name = "my name is erim"
last_name = "serdonmez"
months = ["January", "February","March","April"]
message = "I was born in " + "27th of "+ months[2]  
Months1 = []
subscribers = ["eserdnmez@gmail.com", "example@gmail.com", "mary@gmail.com"]
'''
'''
print(numbers, "\nHello " +name,quote,start.strip())

print(first_name.title()) , print(last_name.title())
'''
### Methods Basic
'''
print(quote.find("away"))
print(quote.replace("burn","live"))
print(months[0]) , print(months[3])
'''
'''
print(message)

answerx = input("What is your name? ")

print("Hello there, " + answerx.title() + " nice to meet you...")

answer = input("May I learn your birthday month please... ")

Months1.append(answer)
print("Thank you very much for your corpartion " + answerx )
print("Your birthday month is " + answer + " is that correct")
'''

####  Pop Method
'''
print(subscribers)

popped_subscriber = subscribers.pop()

print(subscribers)

print(popped_subscriber)

subscribers = ["eserdnmez@gmail.com", "example@gmail.com", "mary@gmail.com"]

first_subscriber = subscribers.pop(0)

print(subscribers)

print("Your first subscriber was " + first_subscriber + ".")

subscribers = ["eserdnmez@gmail.com", "example@gmail.com", "mary@gmail.com"]

subscribed_by_mistake = "eserdnmez@gmail.com"
subscribers.remove(subscribed_by_mistake)
print(subscribers)

print("\nThis person " + subscribed_by_mistake + "did not want to sign up.")
'''

### Organizing a List
### Creating a list of months
'''
birthday_months = ["may", "november", "june"]

birthday_months.sort()
print(birthday_months)

birthday_months = ["may", "november", "june"]
'''
### using reverse method
'''
birthday_months.reverse()
print(birthday_months)
'''
###sorted method - Temporary sorting
'''
birthday_months = ["may", "november", "june"]
print(sorted(birthday_months))
print(birthday_months)
'''
###How to find the lenght of a list
'''
birthday_days =["monday", "tuesday", "wednesday","thursday","friday","saturday","sunday"]

print(len(birthday_days))
'''
###Looping Through a List
'''
months =["January","February","March","April","May","June","July","August","September","October","November","December"]
'''
###For/in loop 
'''
for x in months:
    print(x.title() + " is the name of the month" + "\n")
    print("The next month is: ")
'''

###Numerical Lists
###range function
'''
for value in range(1,5):
    print(value)
'''
#Converting numbers in to a list
'''
numbers = list(range(1,6))
print(numbers)

odd_numbers = list(range(1,101,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
'''
### Slicing a List
'''
birthday_days =["monday", "tuesday", "wednesday","thursday","friday","saturday","sunday"]
'''
'''
print(birthday_days[0:2])
print(birthday_days[1:3])
print(birthday_days[:3])
print(birthday_days[2:])
print(birthday_days[-3:])
'''
### Looping through a Slice 

    #With a For loop
'''
print("Here are the last 3 days of the week")
for i in birthday_days[-3:]:
    print(i.title())
'''
### Copying a List
'''
days = birthday_days[:]
print(days)
'''

###Tuples
###Cannot be changed only overwritten
'''
dates = (1,4,6,11)
coordinates = (1001,5002)
print("Original Coordinates")
for i in coordinates:
    print(i)

coordinates = (2002,7500)
print("\n New Coordinates: ")
for i in coordinates:
    print(i)

'''

### If Statement
'''
print("To continue please log in. ")

password = input("Please enter your password. ")
if password == "Erim":
    print("Access granted. ")
else:
    print("Incorrect. Please try again")
''' 
## Checking multiple conditions and condition
'''
username = input("Welcome Please enter your username. ")
password = input("Please enter your password. ")
if username != "Erim" and password != "123456":
    print("Access denied. ")
else:
    print("Welcome...! ")
'''
### Age Checker (Or Condition)
'''
your_age = input("How old are you? ")
friend_age = input("How old is your friend? ")
if int(your_age) >= 18 or int(friend_age >= 18):
    print("Gratz, one of you is old enough to vote")
else:
    print("Sorry one of you is too young to vote. ")
'''

### Using Or keyword to check values in a list

    #names Registered
'''
registered_names = ("Erim", "frank","Marry", "Peter")

username = input("Please enter username you would like to use. ")
'''
# check to see if username is already taken
'''
if username in registered_names:
    print("Sorry username already taken. ")
else:
    print("Welcome " + username )
'''

### Checking if a value is not in a list
'''    
    #Admin users
admin_users = ("SketchQ", "Sketra")
# ask for a username
username = input("Please enter your username? ")
#Check if user is an admin user
if username not in admin_users:
    print("You do not have access")
else:
    print("Access Granted")
'''

### Interest rate checker using if-elif-else

#Check Balance - only uses one condition
'''
balance = input("What is your bank balance? ")
if int(balance) <= 0:
    print("Would you like to add a deposit? ")
elif int(balance) <=50:
    print("You do not qualify for the interest. ")
elif int(balance) < 100 :
    print("Your interest rate is 1%.")
else:
    print("your interest rather is 2%".title())
'''

### What if you want to use more than one condition
'''
booking_details =["Erim","middle row","screen two"]

if "Erim" in booking_details:
    print("Welcome to my Cinema")
if "middle row" in booking_details:
    print("Your seat number is 010 in the middle row. ")
if "screen two" in booking_details:
    print("Your film is in screen two. ")
'''

### Using if statements with lists

### Creating our shopping cart




shopping_cart = ["pens","stapler","post-its","paper"]

# Adding each item to an order
'''
for item in shopping_cart:
    if item =="pens":
        print("Sorry that item is out of stock ")
    else:
        print("Adding " + item + " to your order. ")
print("Your order is complete. ")
'''

# Working with empty lists

'''
shopping_cart = []
'''
positive_answers = ("Y","y")
negative_answer = ("N","n")
'''
## I would come to this later
answery = input("Would you to add 'Apples' to your shopping cart?...y or n)
if answery in positive_answers :
    shopping_cart.append("Apples")
else:
    print("Thank you for using this app. ")
'''
'''
answer = input("Would you like to add pens to your shopping list?... y or n ")
if answer in positive_answers:
    print("Adding pens to your shopping list. ")
    shopping_cart.append(answer)
    i = input("Thank you, would you like to check out now?... y or n ")
    if i  in positive_answers:
        if shopping_cart:
            for item in shopping_cart:
                print("Your order is complete. ")
    else:
        print("Thank you, have a great day. ")
else:
    print("Thank you,have a great day. ")


if shopping_cart:
    for item in shopping_cart:
        print("Adding " + item + " to your cart")
    print("your order is complete")
else:
     print("You must select an item before proceeding. ")

'''

### Working with multiple lists
'''
in_stock = ["blue pens","paper","staples"]
shopping_cart = ["blue pens","paper","staples","orange post-its"]

for item in shopping_cart:
    if item in in_stock:
        print("Adding " + item + " to your order. ")
    else:
        print("Sory " + item + " is not in stock. ")
print("Your order is complete. ")
'''

### Dictionaries Intro
'''
book_1 = {"author" : "J.R.R.Tolkien", "price" : 10}

print(book_1["author"])
print(book_1["price"])
'''
#Dictionary of terms
'''
terms = {"variable" : "represent or refers to a value stored in memory" , "string" : "a sequence of characters"}

term = {}

term["integer"] = "A Whole number"

print(term["integer"])


if "float" in term:
    print("I know what a float is. ")
else:
    print("I do not know what that is. ")

print(terms["variable"])
'''
## Using get() method with dictinary
    ## you will always get a response with this
'''
print(terms.get("variable"))
print(terms.get("float", "Not in the dictinary"))
'''
### Editing and deleting values in dict.
'''
terms = {"integer" : "Is a number that contains a decimal place" , "string" : "A sequence of characters."}

terms["integer"] = "A whole number"
del terms ["integer"]

print(terms)
'''
### Looping through dictinary
'''
birthday_months = {
    "Erim" : "march",
    "Ertan" : "June",
    "Emine" :"January",
    "Ekin" : "May",
}
for key, value in birthday_months.items():
    print("\nName:" + key)
    print("month:" + value )
'''
#Looping through key-value pairs
'''
book_1 = {
    "name" : "Lord of the Rings",
    "author" : "J.R.R.Tolkien",
    "price" : "14.99",
    "publisher" : "Virgin Books",
}

for key, value in book_1.items():
    print("\nKey :" + key )
    print("value: " + value)
'''
### other ways to loop
'''
for name in birthday_months.keys():
    print(name.title())

for months in birthday_months.values():
    print(months.title())

'''
###Creating a set in dict 
    # Doesnot show the duplicates
'''
for months in set(birthday_months.values()):
    print(months.title())

'''
### Using a dictinary in a list
'''
book_0 ={
    "name" : "harry potter",
    "author": "J.K Rowling",
    "price" : "17,99",
    "publisher" : "Lunatic books"
}
book_1 = {
    "name" : "Lord of the Rings",
    "author" : "J.R.R.Tolkien",
    "price" : "14.99",
    "publisher" : "Virgin Books",
}
book_2 ={
    "name" : "Game of Thrones",
    "author": "G.R.R.Martin",
    "price" : "20,99",
    "publisher" : "Meta Books",
}

books = [book_0, book_1, book_2]


for book in books:
    print(book)

stock_items = []
'''
#Make 50 blue pens
'''
for blue_pen in range(0,50):
    new_blue_pen = {"color" : "blue", "Type" : "Ballpoint", "price" : "5.99"}
    stock_items.append(new_blue_pen)
'''
# Changing the price of the first five pens
'''
for blue_pen in stock_items[0:5]:
    if blue_pen["price"] == "5.99":
        blue_pen['price'] = "1.99"

for blue_pen in stock_items[0:5]:
    print(blue_pen)
'''
### Using list within a dictinary
'''
my_ordered_car = {
    "type" : "standart four door saloon",
    "extras" : ["alloy wheels","climate control","leather heated seats"]
    }
'''
#Print Order Summary
'''
print("The car you ordered is a " + my_ordered_car["type"] + " with the following extras")

for extra in my_ordered_car["extras"]:
    print("\n " + extra)
'''

### Using the input prompt
'''
prompt = ("This is our lecture discussing python's input and how to keep it tidy. Please enter your favourite lecture so far and why you like it? ")

favorite_lecture = input(prompt)

'''

### Using While loops
'''
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1
'''
### To end to program with while loop
'''
prompt = " To end this program enter 'q'. "
prompt +=" Please enter your name: "

message = ""
while message != "q":
    message = input(prompt)
    print(message)
'''

### Using a flag to stop a program
'''
active = True
while active:
    message = input(prompt)
    if message == "q":
        active = False
    else:
        print("its still going...")
'''
### Using a break to break the loop
'''
prompt = "\n Please enter the game you've played recently? "
prompt += "\n To quit press 'q'. "

while True :
    message = input(prompt)
    if message == "q":
        break
    else:
        print( message.title() +  " Nice game that one.")
'''

### Using Continue in a loop
'''
current_number = 0
while current_number < 10:
    current_number += 1
# If the current number divided by 2 has a remainder of zero, then print the current number and continue the loop
    if current_number % 2 == 0:
        continue

print(current_number)
'''

###Working with while loops and lists

'''
uncomfirmed_users = ["erim", "Ekin","Emine","Ertan"]
confirmed_users = []

while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)


print("\n Following users have been confirmed: ")
for i in confirmed_users:
    print(i.title())
'''

### Removing Values from a list

books = ["lotr","Game of Thrones","Harry Potter","Perfume","Harry Potter", "Harry Potter"]
new_books =[]
'''
while "Harry Potter" in books:
    books.remove("Harry Potter")

print(books)
'''
### To remove the duplicates
'''
for i in books:
    if i not in new_books:
        new_book = i
        new_books.append(i)

print(new_books)
'''
###Adding user input to dictionary
'''   
   
    #Create an empty dictionary
rental_properties = {}
    #Set a fliag to indicate we taking applications
rental_open = True

while rental_open :
    #promp users for user name and adress
    username = input("What is your name? ")
    rental_property = input("What is the address of the property you would like to rent")

    #Store the response in a dictionary
    rental_properties[username] = rental_property
    # ask if the user knows anyone else looking to rent a property
    repeat = input("\n Do you know anyone else who wants to user our application? ")
    if repeat ==  "no" :
        rental_open = False
        
   
print("\n -----Property to Rent----")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " To rent. ")
'''
'''
user_list = {}
subscribers = []


username = input("\nWhat is your username? ")
email_adress = input("\n What is your email adress? ")

user_list[username] = email_adress

repeat = input("Would you like to subscribe to our newsletter? ....'y' or 'n'")
if repeat == 'y':
    email = user_list.pop(username)
    print("Adding " + username + " to the subscribers list. ")
    subscribers.append(email)
else:
    print("Thank you for signing up. ")

print(user_list)
print(subscribers)
'''

###Function

'''
def formatted_name(First_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name  + " " + middle_name  + " " + last_name
    else:
        full_name = first_name  + " " +  last_name
    return full_name.title()

teacher = formatted_name("Erim", "Serdonmez")

print(teacher)
'''

### Using a While loopin in a function
'''
def get_formatted_name(first_name, last_name):
    #Return a full name neatly formatted.
    full_name = first_name + " " + last_name
    return full_name.title()




while True:
    print("\n What is your name? ")
    print("\n Press 'q' to quit anytime to quit this program. ")
    first_name = input("First Name: ")
    if first_name == "q":
        break
    last_name = input("last Name: ")
    if last_name == "q":
        break
    x=get_formatted_name(first_name, last_name)
    print("\n Hello " + x + " .")
'''

### Passing a list to a function
'''
def books_available(books):
    #show a list of books available to buy
    for book in books:
        books_in_stock = "The following title is available to buy " + book.title() + " ."
        print(books_in_stock)

available_books = ["Lotr","Harry Potter", "Game of Thrones", "Perfume"]
books_available(available_books)
'''
### Airline Check-in procedure
'''
def passangers(not_checked_in, checked_in):
    #simulate passangers who are not checked in
    
    while not_checked_in:
        current_passanger = not_checked_in.pop()
        #Simulate checking a passanger in
        print("Checking in passanger: " + current_passanger + " .")
        checked_in.append(current_passanger)

def show_checked_in_passangers(checked_in):
    #show all passangers who have checked in
    print("\n The following passangers have been checked in ")
    for passanger in checked_in:
        print(passanger)


not_checked_in = ["Erim Serdönmez","Ekin Serdönmez","Emine Aydın","Ertan Serdönmez"]
checked_in = []

passangers(not_checked_in, checked_in)
show_checked_in_passangers(checked_in)
'''

#### Keeping a copy of the item from original list
'''
passengers(listname][:])

passengers(not_checked_in[:], checked_in)
'''

### arbitary arguments
'''
def create_passengers(*requests):
    #print user requests
    print("\n This passenger has requested: ")
    for request in requests:
        print("- " + request)

create_passengers("next to window","close to entrance","pre-order breakfast/meal")
'''

### Using positional and arbitrary arguments together
'''
def assing_seat(seat, *requests):
    #assing a seat and request to a passenger
    print("\n Assign seat number " + str(seat) + " the following request(s)")
    for request in requests:
        print("-" + request)

assing_seat(36, "window seat","pre paid breakfast")
'''

###Using arbitrary keyword arguments
'''
def seat_profile(first, last, **passenger_info):
    #Build a dictionary containing passenger info
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in passenger_info.items():
        profile[key] = value
    return profile

passenger_info = seat_profile("Erim", "Serdönmez", seat_number = 27, pre_paid_meal = True)

print(passenger_info)
'''

###Classes
    # Creating the first Class
'''
class Book():
    # A class to create a book

    def __init__(self, name, price, publisher):
        #Initialize the name, price and publisher attributes

        self.name = name
        self.price = price
        self.publisher = publisher
    def hardback(self):
        #simulate a hardback book
        print(self.name.title() + " is a hardback book")
    def softback(self):
        #simulate a book being a softback
        print(self.name.title() + " is a softback book")

    def ebook(self):
        #simulate an ebook
        print(self.name.title() + " is an ebook")

    def ebook_reader(self):
        #Simulate an ebook reader
        print("Library: " + self.name.title() + str(self.price) + self.publisher.title() +" .")
'''
'''
#Creating an instance of our book class.
my_book = Book('Lord of the Rings', 14.99, 'Meta Yayın')
your_book = Book("Game of thrones", 25.99 , "Kopi paest yayın")
## Accesing atributes of the class
'''
'''
print("I'm currently reading " + my_book.name.title())
print("This book costs " + str(my_book.price) + " .")
print("This book publishe by " + my_book.publisher.title() + " .")
print("This book's name is: " + your_book.name.title() + " .")

my_book.ebook()
'''
###Calling our ebook_reader method

'''
### Creating a new ereader class
'''
'''
class Ereader():
    #A class to represent an ereader

    def __init__(self,make,model,backlight,battery_life,screen_type):
        #initialize the attributes to describe an ereader
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery_life = battery_life
        self.screen_type = screen_type
        self.library_count = 0

    def get_ereader_name(self):
        #return a formatted descriptive name for our ereader
        long_name = self.make + " " + self.model + " " + self.backlight + " " + self.battery_life + " " + self.screen_type
        return long_name.title()
    def read_library_count(self):
        print("You have " + str(self.library_count) + " books in your Amazon kindle library")
    def update_library_count(self, ebook_count):
        #set the library count
        self.library_count = ebook_count
    def increment_library_count(self,purchased_ebook):
        #adding purchased ebook to our library count
        self.library_count += purchased_ebook
'''
'''
my_new_ereader = Ereader("Amazon kindle", "Paperwhite", "adjustable backlight", "several months of battery life","300dpi")

print(my_new_ereader.get_ereader_name())
my_new_ereader.read_library_count()


##Modifying the attribute(s) directly
my_new_ereader.library_count = 45 # changed the value of the attribute.
my_new_ereader.read_library_count()

###Modifying the attribute through methods

my_new_ereader.update_library_count(54)
my_new_ereader.read_library_count()

### Incremental change in value

my_new_ereader.increment_library_count(3)
my_new_ereader.read_library_count()
'''
###Creating a Child class
'''
class Screen():
    #Create class to model the screen of a kindlefire

    def __init__(self,screen_resulation = "1280 * 800"):
        ###Initilize the screen attributes
        self.screen_resulation = screen_resulation

    def describe_screen(self):
    #Print out some marketing copy about the kindlefire
        print("Fire HD 8 features a widescreen " + self.screen_resulation + " HD screen")





class KindleFire(Ereader):
    #represents aspects of an ereader specific to a kindle Fire
    #Then initialize atributes specific to a KindleFire

    def __init__(self,make,model,backlight,battery_life, screen_type):

        super().__init__(make,model,backlight,battery_life,screen_type)
        self.firescreen = Screen()


 

my_kindle_fire = KindleFire("amazon","kindle fire","backlight","12 hour battery life","color")
print(my_kindle_fire.get_ereader_name())

my_kindle_fire.firescreen.describe_screen()
'''
        ####-----FILES------###
### Read an entire file
'''
file_path = "/users/devil/desktop/Python Beginners Code and Basics/My Python Documents/movies.txt"
filename = "/users/devil/desktop/Python Beginners Code and Basics/My Python Documents/movies_line_by_line.txt"

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.strip())

with open(filename) as file_object1:
    for line in file_object1:
        print(line.strip())
'''
### Making a list from a file
'''
new_list = []
with open(filename) as file_object2:
    lines = file_object2.readlines()
   
for line in lines:
    print(line.strip())


print("\n-------------------------------------\n")

for line in lines:
    print(line.strip())

print("\n-------------------------------------\n")
popped_movie = lines.pop()

print(popped_movie)
lines.append(popped_movie)

print("\n-------------------------------------\n")

sorted_list = lines.sort()

for line in lines:
    print(line.strip())


file_name = "Programming.txt"

with open(file_name, "w") as file_object3:
    file_object3.write("This is a test")


message = input("What is your favorite program? ")

with open(file_name, "a") as file_object:
    file_object.write("\n" + message)
'''

        #### EXCEPTIONS ###
##Zero divison error
'''
print(5/0)
'''
## try except block
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero. ")
'''
### The else block
'''
print("Please enter two numbers to be divided? ")
print("Enter 'q' to quit. ")

while True:
    first_number = input("\n First Number:   ")
    if first_number == 'q':
        break
    second_number = input("\n Second Number:   ")
    if second_number == 'q':
        break
   
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero. ")
    else:
        print(answer)

'''
### File not found error
'''
try:
    with open("movies.txt") as file_object:
        contents = file_object.read()
        print(contents.strip())
except FileNotFoundError:
    message = "Sory, the file 'movies' can not be find"
    print(message)
'''

###Analyzing text
'''
def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        #message = "Sorry, The file " + filename + " can not be found."
        #print(message)
    else:
        words = contents.split()
        number_words = len(words)
        print("The file " + filename + " has roughly " + str(number_words)+ " words.")

filenames = ["heathcliff.txt", "Moby Dick.txt"]
for filename in filenames:
    word_count(filename)
'''

### Working with json.dump() function
'''
import json

phone_number = (1234567890)

filename = "phone_number.json"
with open(filename, "w") as file_object:
    json.dump(phone_number, file_object)
'''
'''
### Working with json.load()

with open(filename) as file_object:
    phone_number = json.load(file_object)

print(phone_number)
'''

### Storing and reading user Data

'''
import json
username = input("What is your username? ")
filename = "username.json"

with open(filename, "w") as file_object:
    json.dump(username, file_object)
    print("Thank you, I will remember you " + username)

filename = "username.json"
with open(filename) as file_object:
    username = json.load(file_object)

print( "Welcome back " + username + " .")
'''

###Combining the above two codes into one(Refactoring)
'''
file_name = "username.json"

try:
    with open(file_name) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your username? ")
    with open (file_name, "w") as file_object:
        json.dump(username,file_object)
        print("Thank you for signing up I will remember you " + username + " for future referance ")
else:
    print("Welcome Back " + username + " !!!") 
'''

#### Test function

def get_formatted_name(first,last):
    full_name = first +" " +last
    return full_name.title()
'''
print("Enter 'q' to exit the program ")

while True:
    first = input("What is your first name: ")
    if first == 'q':
        break
    last = input("What is your last name? ")
    if last == 'q':
        break
    full_name= get_formatted_name(first,last)
    print("Your name is " + full_name.title())   
'''
import unittest

class NamesTestCase(unittest.TestCase):
    #Test for the test function 1
    def test_first_last_name(self):
        #test first and last names
        formatted_name = get_formatted_name("erim","serdönmez")
        self.assertEqual(formatted_name, "Erim Serdönmez")

unittest.main()



