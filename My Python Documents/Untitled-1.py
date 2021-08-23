
'''
for i in range(0,10):
    if i ==0:
        sum = i 
        print("Current Number: " + str(i) + " Previous number " + str(i) +" Sum is : " + str(sum))
    else:
        sum = i + i-1
        print("Current Number: " + str(i) + " Previous number " + str(i-1) +" Sum is : " + str(sum))
    
'''

'''
string = "pynative"

output = list(string)
print(output[::2])

def removeChars(str,n):
    if int(n) > len(str):
        print("You cant do that ")    
    else:
        return string[n:]

print(removeChars(string,4))

'''

'''listA =[10, 20, 30, 40, 10]
listB = [10, 20, 30, 40, 50]
listC = [10,50,40,30,20,20,50,10,80,100,10]

def compareLists(list):
    n = len(list) -1
    if list[0] == list[n]:
        return True
    else:
        return False

print(compareLists(listA))
print(compareLists(listB))
print(compareLists(listC))
'''
'''list =  [10, 20, 33, 46, 55]

def div5(list):
    for i in list:
        if ( i % 5 == 0):
            print(i)                           
           
div5(list)

'''

'''string = "Emma is good developer. Emma is a writer"
print("Emma has apperead " + str(string.count("Emma")) + " times.")
'''


'''
print("1" "\n2 2 " "\n3 3 3 " "\n4 4 4 4 " "\n5 5 5 5 5 ")

for i in range(1,6):
    print(i)'''

'''import random

spam = random.randint(1,3)

if spam == 1:
    print("Hello ")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings...")'''


'''for i in range(1,11):
    print("This are the numbers: " + str(i))

i = 1
while i < 11:
    print("These are the numbers: " + str(i))
    i = i + 1
    if i == 11:
        break'''

'''x = abs(-7.25) # retunrns the exact value of a value (like ignores negatives)
print(x)
y = abs(3-5)
print(y)'''

'''for i in range(6):
    print(str(i)* i)'''
    

'''def fund(value):
    if len(value) == 1:
        return value[0]
    return '{}, and {}' .format("," .join(value[:-1]), value[-1])

spam = ["apples", "bananas", "tofu","cat"]
bacon = []
print(fund(spam))
print(fund(bacon))'''

'''import random


coinFlip = []
streak = 0
numberOfStreaks = 0
for i in range (11):
    for y in range(6):
        coinFlip.append(random.randint(0,1))
for i in range(len(coinFlip)):
    if i == 0:
        pass
    elif coinFlip[i] == coinFlip[i-1]:
        streak += 1
    else:
        streak = 0
    if streak == 6:
        numberOfStreaks += 1
print(coinFlip)
print(streak)
print(numberOfStreaks)'''




'''def compareNumbers(num):
    print("original number ", num)
    originalNum = num
    revs_number = 0
    while (num > 0):
        remainder = num %10
        revs_number = (revs_number *10) + remainder
        num = num // 10
    if (originalNum == revs_number):
        return True
    else:
        return False

print("The original and reverse number is the same " , compareNumbers(121))'''    

'''chessBoard = {"1a":" ","1b":" ","1c":" ","1d":" ","1e":" ","1f":" ","1g":" ","1h":" ",
"2a":" ","2b":" ","2c":" ","2d":" ","2e":" ","2f":" ","2g":" ","2h":" ",}'''



import sys

print(sys.version)
print(sys.path)