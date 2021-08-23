###Python basic (Part -I) [150 exercises with solution]
### url = https://www.w3resource.com/python-exercises/python-basic-exercises.php
### Erim Serdönmez
### 25/06/2021


# 1.
'''
print("Twinkle, twinkle, little star," "\n""\tHow I wonder what you are!" "\n""\t\tUp above the world so high,""\n\t\tLike a diamond in the sky." "\nTwinkle, twinkle, little star,""\n\tHow I wonder what you are" )
'''
# 2.Write a Python program to get the Python version you are using.
    #Note : 'sys' module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
'''
import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)
'''
# 3.Write a Python program to display the current date and time.
'''
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
'''
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area
'''
from math import pi
r = float(input(" Please enter the radios of the circle you would like to know the area of: "))
print("The area of the circle with a radios of " + str(r) + " is: " + str(pi * r **2))
'''
# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
'''
first = input("what is your name? ")
last = input("What is your lastname? ")

full_name = last + " " + first
print(full_name.title())
'''
# 6.  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
'''
values = input("Please enter some comma seperated numbers: ")
list = values.split(",")
tuple= tuple(list)
print("list: ", list)
print("Tuple: ", tuple)
'''
# 7. Write a Python program to accept a filename from the user and print the extension of that
        #Python str.rsplit(sep=None, maxsplit=-1) functionThe function returns a list of the words of a given string using a separator as the delimiter string.If maxsplit is given, the list will have at most maxsplit+1 elements.If maxsplit is not specified or -1, then there is no limit on the number of splits.If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.The sep argument may consist of multiple characters.Splitting an empty string with a specified separator returns [''].
'''
answer = input("Please enter the filename with the extension to see the output ")
f_extns = answer.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
'''
# 8. Write a Python program to display the first and last colors from the following list color_list = ["Red","Green","White" ,"Black"]
'''
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0]), print(color_list[3])
'''
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)
'''
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" %exam_st_date)
'''
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''
n = int(input("Please enter the value of 'n' : "))

n1 = int("%s" % n)
n2 = int("%s%s" %(n,n))
n3 = int("%s%s%s" % (n,n,n))
print(n1+n2+n3)
'''
# 11. 