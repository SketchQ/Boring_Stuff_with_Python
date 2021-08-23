## Automate the Boring stuff examples with my answers
## Erim Serdönmez

## ------------------------- Chapter 1 Basics --------------------------------------##

# 1. Which of the following operators, and which are values?
'''
* =>    OPERATOR
'hello'=> VALUE
-88.8 => VALUE
- => OPERATOR
/ => OPERATOR
+ => OPERATOR
5 => VALUE
'''
# 2. Which of the following is a variable, and which is a string?
'''
spam   =>   VARIABLE
'spam' =>   STRING
'''
# 3. Name three data types.
''' Integer,String and Boolean
'''
# 4. What is an expression made up of? What do all expressions do?
''' expressions are made out of values and operators and they evaluate to a single value.
'''
# 5. This chapter introduced assignment statements, like spam=10. What is the differance between an expression and a statement?
''' Expressions evaluate to a single value whereas statements do not evaluate.
'''
# 6. What does the variable 'bacon' contain after the following code runs?
''' bacon = 20
bacon + 1
bacon contains the value '21' after the above code runs.
'''
''' Bacon + 1 expression does not reassing the value in bacon therefore it still is 20'''
# 7. What should the following two expressions evaluate to?
''' 'spam' + 'spamspam' =>  'spamspamspam'
    'spam' * 3          =>  'spamspamspam'
'''
# 8. Why is 'eggs' avalif variable name while 100 is invald?
''' variables cannot beging with numbers although they might end with one.In this case '100' is an integer value and cannot be given any other value other than itself.
'''
# 9. What three functions can bu used to get the integer,floating-point number, or string version of a value?
''' int() for integer values, float() for floating-point numbers and str() for string values.
'''
# 10. Why does this expression cause an error? How can you fix it?
''' 'I have eaten' + 99 + 'burritos.'  => Well, you cannot concanate str with int or vice versa. So we need to use str() function to turn 99 into a string value. 
Which is : 'I have eaten ' + str(99) + ' burritos.' 
'''

## ------------------------- Chapter 2 Flow Control --------------------------------##

# 1. What are the two values of the Boolean data type? How do you write them?
'''
 True and False , you write them with the first letter as capital remaining as lowercase like = 'True' and 'False'
'''
# 2. What are the three Boolean operators?
'''
(and,not, or) are the three boolean operators
'''
# 3. Write out the truth tables of each Boolean operator ( that is, every possible combination of Boolean values for the operator and what they evaluate to.)
'''
True and True = True        True or True = True     not True = False
True and False = False      True or False = True    not False = True
False and True = False      False or True = True
False and False = False     False or False = False
'''
# 4. What do the following expressions evaluate to?
    # (5>4) and (3==5)      
    # not (5>4)
    # (5>4) or (3==5)
    # not ((5>4) or (3==5))
    # (True and True) and (True == False)
    # (not False) or (not True)
''' False
    False
    True
    False
    False
    True
'''
# 5. What are the six comparison operators?
'''
==      Equal to
!=      not Equal to
>       Greater Than
<       Lesser than
>=      Greater or equal to
<=      Lesser or equal to
'''
# 6. What is the difference between the equal to operator and the assignment operator?
'''
'=' operator which is the assignment operator sets the value to a variable whereas '==' operator or equal to operator checks the value of two values and compares them with each other.
'''
# 7. Explain what a condition is and where you would use one.
'''
Conditions are expressions which evaluates to a Boolean value. In which we can use it with 'if' or 'While' loops to make our programs much more smarter and detailed.
'''
# 8. Identify the three blocks in this code:
    # spam = 0
    # if spam == 10:        First one begins
    #   print('eggs')
    #   if spam > 5:        Second one begins
    #       print('bacon')  
    #   else:               Third one begins
    #       print('ham)     Third one ends
    #   print('spam')       second one ends
    # print('spam')         First one ends.

# 9. Write code that prints 'Hello' if 1 is stored in spam, prints 'Howdy' if 2 is stored in spam, and print 'Greetings' if anything else is stored in spam.
'''import random
spam = random.randint(0,3)
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')'''
# 10. What keys can you press if your program is stuck in an infinite loop?
'''
Ctrl + C
'''
# 11. What is the difference between 'break' and 'continue'?
'''
'break' will exits the loop and will not re-check the condition.
'continue' will jump back to the start of the loop and will re-check the condition.
'''
# 12. What is the difference between range(10), range(0,10), and range(0,10,1) in a for loop?
'''
range(10) = will start from 0 and will go up to 9 (not including 10) in a default step (meaning n, n+1)
range(0,10) = will start from 0 and will go up to 9 (not including 10) in a default step. Basically we are giving it a starting point but because default starting value is set to zero, it will not make any difference to the one above.
range(0,10,1) = will start from 0 and will go up to 9 (not including 10) but this time we are giving it a step value which is set to (n, n+1) 
'''
# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
'''for i in range(1,11):
    print(i)
i = 0
while i <= 10:
    i += 1
    print(i)
    if i == 10:
        break'''
# 14. If you had a function name bacon() inside a module named spam, how would you call it after importing spam?
'''
spam.bacon()
'''

## ------------------------- Chapter 3 Functions ----------------------------------##

# 1. Why are functions advantageous to have in your programs?
'''
Major purpose of functions isto group code that gets repeated in order to avoid copy-paste
'''
# 2. When does the code in a function execute: When the function is defined or when the function is called?
'''
When the function is called then it executes
'''
# 3. What statement creates a function?
'''
def statement
'''
# 4. What is the difference between a function and a function call?
'''
Function call executes the function whereas function is a defined group of code that doesn't change.
'''
# 5. How many global scopes are there in a Python program? How many local scopes?
'''
Theres only one global scope in Python program but local scope may vary depending on how many function does exist in that program.
'''
# 6. What happens to variables in a local scope when the function call returns?
'''
They got destroyed or deleted 
'''
# 7. What is a return value? Can a return value be part of an expression?
'''
The value that function evaluates is called a return value. Return values can be expressions.
'''
# 8. If a function does not have a return statement, what is the return value of a call to that function?
'''
None
'''
# 9. How can you force a variable in a function to refer to the global variable?
'''
with global keyword statement
'''
# 10. What is the data type of None?
'''
its None datatype
'''
# 11. What does the import areallyourpetsnamederic statement do?
'''
imports module called areallyourpetsnamederic
'''
# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
'''
spam.bacon()
'''
# 13. How can you prevent a program from crashing when it gets an error?
'''
With try and except blocks
'''
# 14. What goes in the try clause? What goes in the except clause?
'''
In try clause there will be a code which the program will try to run, and on the except clause, if the try clause had caused an error which was specified in the except clause, except clause will be executed.
'''


## -------------------------- Chapter 4 Lists ---------------------------------------------##

# 1. What is [] ?
'''
its a square bracket which defines a list, right now its an empty list.
'''
# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named 'spam' ? (Assume spam contains [2,4,6,8,10].)
'''
spam.insert(2,'hello') // spam[2] = 'hello'
'''
# 3. What does spam[int(int('3'*2)//11)] evaluate to ?
'''
it will evaluate to 3 
'''
# 4. What does spam[-1] evaluate to? 
'''
Final item of the list
'''
# 5. What does spam[:2] evaluate to?
'''
From beginning of the list untill the second item which is not included. Example spam = [2,4,5,6,6] ==> spam[:2] ==> 2,4
'''
# For the following three questions, let's say 'bacon' contains the list [3.14,'cat',11,'cat',True].
    # 6. What does 'bacon.index('cat') evaluate to?
'''
     to 1 
'''
    # 7. What does 'bacon.append(99)' make the list value in 'bacon' look like?
'''
    [3.14,'cat',11,'cat',True,99]
'''
    # 8. What does 'bacon.remove('cat')' make the list value in 'bacon' look like ? 
'''
    [3,14,11,'cat',True]
'''
# 9. What are the operators for list concatenation and list replication?
'''
'+' concanetes two list into one
'*' replicates that list 
'''
# 10. What is the difference between the 'append()' and 'insert()' list methods?
'''
append() will add that item at the end of the list while insert() will add the item to a indicated position
'''
# 11. What are two ways to remove vales from a list?
'''
del statement with the index number and remove() method. Ex ==> del spam[1] and spam.remove('cat')
'''
# 12. Name a few ways that list values are similar to string values.
'''
like lists we may consider strings as a list of letters, therefore a lot of the list methods will also work on strings.Such as: Indexing,slicing,for loops, in,not in, and len()
'''
# 13. What is the difference between lists and tuples?
'''
list are mutable while tuples are immatuble
'''
# 14. How do you type the tuple value that has just the integer value 42 in it?
'''
tuple = (42,)
'''
# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
'''
using the list() and tuple() functions respectively.
'''
# 16. Variables that 'contain' list values don't actually contain lists directly. What do they contain instead?
'''
They contain the referance of that list instead of the list itself
'''
# 17. What is the diference between 'copy.copy()'and 'copy.deepcopy()' ? 
'''
copy.copy() will just copy the reference of that list while copy.deepcopy() will create an another reference object.
'''
## ------------------------- Chapter 11 DEBUGGING ----------------------------------##

# 1. Write an 'assert' statement that triggers an 'AssertionError' if the variable 'spam' is an integer less than 10.
'''import random

spam = random.randint(5,20)
print(spam)
assert spam > 10 ,"Number has to be bigger than 10"'''
    

# 2. Write an 'assert' statement that triggers an 'AssertError' if the variables 'eggs' and 'bacon' contain string that are the same as each other, even if their cases are different (That is, 'hello' and'hello' are considered same, and 'goodbye' and 'goodBYE' are also considered same.)

'''eggs = 'Hello'
bacon = 'goodbye'

if eggs and bacon:
    eggs = 'GOODbye'

assert (eggs.lower() != bacon.lower()), "Well they\'re both the same"'''

# 3. Write an 'assert' statement that 'always' triggers an AssertionError.

'''assert 0>1, "This will always be wrong"'''

# 4. What are the two lines that your program must have in order to be able to call logging.debug()?

''' import logging
logging.basicConfig(level=logging.DEBUG,'format=%(Asctime)s - %(levelname)s - %(message)s')
'''

# 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

'''import logging
logging.basicConfig(filename='programLog.txt',level=logging.DEBUG,'format=%(Asctime)s - %(levelname)s - %(message)s')
'''

# 6. What are the five logging levels?

''' from lowest to highest:
1. debug
2. info
3.warning
4.error
5.critical
'''

# 7. What line of code can you add to disable all logging messages in your program?
''' import logging
logging.disable(login.CRITICAL)
'''
# 8. Why is using loggin messages better than using 'print()' to display the same message?
''' After end of the program when you want to clear the log messages, you will need to carefully look into each print() function. 
Which might be tedious as well as you may end up changing some other print() line that is not a debug log but was a usefull line
With using the logging.LEVEL function you can disable all of them with one line once you're done with them.
'''
# 9. What are the differences between the Step Over, Step in and Step Out buttons in the debugger?
''' Step Over, will step over the line in the code and will move in to the next line (such as functions etc.)
Step in, will go inside the line of code instead of moving to the next line (mostly functions).For example, line might go from line 102 to line 90, becouse theres a function at line 90.
Step out, will step out from the line of code and jump into the next line of code based on the execution order. For example from line 102 to line 90 (Because of funtion), then step in will move into line 91 but step out will skip the lines after 90 instead will jump into line 103 where the code continues.
'''
# 10. After you click Continue, when will debugger stop?
''' Will continue until it finds a breakpoint else it will contine until it executes all lines of code. Effectively to the end of program.
'''
# 11. What is a breakpoint?
''' A point in your code which you want your debugger to jump to
'''
# 12. How do you set a breakpoint on a line of code in Visiual Studio?
'''Click the left area on the screen next to the line once a red dot appears when you mouse-over.
'''

## -------------------------- CHAPTER 12 WEB SCRAPING -----------------------------------##

# 1. Briefly describe the differences between the 'webbrowser,requests,bs4,and selenium' modules.
''' webbrowser = opens up a specific web page
    requests = Download files and webpages from the internet.
    bs4 = parses HTML pages
    selenium = Launches and controls the web page able to simulate mouse clicks on the web page as well.
'''
# 2. What type of object is returned by 'requests.get()'? How can you access the downloaded content as a string value?
''' it will take stirng of URL and will return a 'RESPONSE' object.
'''
# 3. What 'requests' method checks that the download worked?
'''res.raise_for_status() method, if nothing happens after you run this method, that means it worked. It will raise an exception if something is wrong. 
'''
# 4. How can you get the HTTP status code of a 'requests' response?
'''res.status.code = If it is 200, that means it is correct and it worked. You may also try res.status.code == request.codes.ok If this evaluates to True thats also means it worked.
'''
# 5. How do you save a 'requests' response to a file?
'''filename = open('filename.txt','wb') = first you need to open the file with open() function as a binary write mode with 'wb' as second argument.
then you can use iter_content() method to write chuncks of that weppage into that file;
for chunk in res.iter_content(100000):
    filename.write(chunk)
'''
# 6. What is the keyboard shortcut for opening a browser's developer tools?
''' F12
'''
# 7. How can you view ( in the developer tools) the HTML of a specific element on a web page?
''' Right click on that object and select inspect or ctrl+shift+i
'''
# 8. What is the CSS selector string that would find the element with an 'id' attribute of 'main'?
'''soup.select('#main')
'''
# 9. What is the CSS selector string that would find the elements with a CSS class of 'highlight'?
''' soup.select('.highlight')
'''
# 10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
''' soup.select('div div')
'''
# 11. What is the CSS selector string that would find the <button> element with a 'value' attribute set to 'favorite'?
''' soup.select('favorite[type="button"]') \\ soup.select('button[value="favorite"]')
'''
# 12. Say you have a BeautifulSoup 'tag' object stored in a variable 'spam' for the element <div>Hello,world!<\div>. How could you get a string 'Hello,world!' from the 'tag' object?
''' spam[0].getText()   \\ spam.getText()
'''
# 13. How would you store all the attributes of a BeautifulSoup 'tag' object in a variable named 'linkElem'?
''' linElem = soup.select('spam')[0]    \\ linkElem.attrs
'''
# 14. Running import selenium doesn't work. How do you properly import the selenium module?
''' from selenium import webdriver
'''
# 15. What's the difference between the find_element_* and find_elements_* methods?
''' find_element_* ==> will return a single WebElement object ,representing the first element on that webpage that matches your querry
    find_elements_* ==> will return list of WebElement objects, for every matching object on that website.
'''
# 16. What methods do Selenium's WebElement objects have for simulating mouse clicks and keyboard keys?
''' click() method for mouse clicks
    send_keys() method for keyboard keys
    for special keys you need to use a different module which is ;
    from selenium.webdriver.common.keys import keys
    then use the Keys keyword like below:
    Keys.UP, Keys.DOWN,Keys.LEFT,Keys.RIGHT ==> keyboard arrow keys etc...
'''
# 17. You could call send_keys(Keys.ENTER) on the submit button's WebElement objet, but what is an easier way to submit a form with 'selenium'?
'''Just calling the submit() method on any elements will also have the same results as clicking or sending keys to the submit button.
'''
# 18. How can you simulate clicking a browser's Forward,Back and Refresh buttons with 'selenium'?
''' browser.back() ==> For back button
    browser.forward() ==> For forward button
    browser.refresh() ==> For refresh button
'''
## ------------------------------- Chapter 13 Excel -----------------------------------##

# For the following questions, imagine you have a Workbook object in the variable = wb
# A Worksheet object in variable = sheet
# A Cell object in variable = cell
# A Comment object in variable = comm
# An Image object in variable = img

# 1. What does the 'openpyxl.load_workbook() function return?
'''
It returns a Workbook Object
'''
# 2. What does the 'wb.sheetnames' workbook attribute contain?
'''
It contains a list of all sheet names in the workbook // It contains a Worksheet Object
'''
# 3. How would you retrieve the 'Worksheet' object for a sheet named 'Sheet1'?
'''
sheet = wb['Sheet1']
'''
# 4. How would you retrieve the 'Worksheet' object for the workbook's active sheet?
'''
sheet = wb.active
'''
# 5. How would you retrieve the value in the cell C5?
'''
sheet['C5'].value
'''
# 6. How would you set the value in the cell C5 to "Hello"?
'''
sheet['C5'] = 'Hello'
'''
# 7. How would you retrieve the cell's row and column as integers?
'''
sheet['C5'].coordinate  // cell.row and cell.column
'''
# 8. What do the 'sheet.max_column' and 'sheet.max_row sheet' attributes hold, and what is the data type of these attributes?
'''
They hold intgers values for the max column and max row of the sheet.They are integer data types.
'''
# 9. If you needed to get the integer index for column 'M', what function would you need to call?
'''
openpyxl.utils.cell.column_index_from_string('C5')
'''
# 10. If you needed to get the string name for column 14, what function would you need to call?
'''
openpyxl.utils.cell.get_column_letter(14)
'''
# 11. How can you retrieve a tuple of all the 'Cell' objects from A1 to F1?
'''
sheet['A1:F1']
'''
# 12. How would you save the workbook to the filename 'example.xlsx'?
'''
wb.save('example.xlsx')
'''
# 13. How do you set a formula in a cell?
'''
Same as setting a value for the cell, Example
    sheet['C1'] = '=SUM[A1:B4]
'''
# 14. If you want to retrieve the result of a cell's formula instead of the cell's formula itself, what must you do first?
'''
sheet['C1'].value   // When calling load_workbook(), pass True for the data_only keyword argument.
'''
# 15. How would you set the height of row 5 to 100 ?
'''
for i in range(5,101):
    sheet.row_dimensions[i] = 200
//
sheet.row_dimension[5] = 100
'''
# 16. How would you hide column C?
'''
sheet.column_dimension['C'] = 0 // sheet.column['C'].hidden = True
'''
# 17. What is a freeze pane?
'''
Frozen rows or frozen columns are always visible to the user
'''
# 18. What five functions and methods do you have o call to create a bar chart?
'''
1. Create a reference object with openpyxl.chart.Reference() function
2. Create a Series object by passing in the reference object
3. Create a chart object via openpyxl.chart.BarChart()
4. Append the series obj to chart obj
5. Add the chart object to Worksheet obj
///
openpyxl.chart.Reference(), openpyxl.chart.Series(), openpyxl.chart.BarChart(), chartObj.append(seriesObj), and add_chart()

'''
## ----------------- Chapter 14: Working With Google Spreadsheets --------------------------##

# 1. What three files do you need for EZSheets to acces Google Sheets?
'''
credentials-sheets.json
token-drive.pickle
toen-sheets.pickle
'''
# 2. What two types of objects does EZSheets have?
'''
Spreadsheet object and Sheet object
'''
# 3. How can you create an Excel file from a google Sheet spreadsheet?
'''
with downloadAsExcel()
'''
# 4. How can you create a Google Sheet Spreadsheet from an Excel file?
'''
with upload() 
'''
# 5. The ss variable contains a spreadsheet object. What code will read data from the cell B2 in a sheet title "Students"?
'''
sheet = ss['Students']          // ss['Students']['B2']
sheet['B2'] or sheets(2,2)
'''
# 6. How can you find the column letters for column 999 ? 
'''
with sheet.getColumnLetterOf(999)
'''
# 7. How can you find out how many rows and columns a sheet has?
'''
sheets.columnCount and sheets.rowCount
'''
# 8. How do you delete a spreadsheet? Is this deletion permament?
'''
you can delete it with .delete() method for the Sheet object. No its not permanent it will only move to /drive/trash in order to permanently delete you need to enter the keyword permanent=True for the argument of delete() method
'''
# 9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?
'''
ss = ezsheets.createSpreadsheet() this will create a new blank spreadsheet
sheet = ss.createSheet() this will create a new sheet
'''
# 10. What will happen if, by making frequent read and write requests with EZSheets,you exceed your Google account's quota?
'''
It will raise googleapiclient.errors.HttpError “Quota exceeded for quota group” exception but ezsheet will catch this exception and retry the request if not succesfull it will re-raise the exception
'''

## --------------------- Chapter 15: Working With PDF and Word Documents ------------------##

# 1. A string value of the PDF filename is not pased to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?
'''
We need to pass the PdfFile object which we open with read-binary mode and pass it to the PyPDF2.PdfFileReader() function.
///
A file object returned from open()
'''
# 2. What modes do the File Objects for PdfFileReader() and PdfFileWriter() need to be opened in?
'''
read-binary mode 'rb'. If we want to write into that file with writer object we need to open that in write-binary mode 'wb'
'''
# 3. How do you acquire a Page object for page 5 from a PdfFileReader object?
'''
PdfFileReaderObj.getPage(4), with getPage() method which is zero based meaning it starts at 0 and not 1 therefore; page 5 is page 4
'''
# 4. What PdfFileReader variable stores the number of pages in the PDF document?
'''
Zero-based integers
///
the numPages variable stores an integer of the number of pages in the PdfFileReader object.
'''
# 5. If a PdfFileReader object's PDF is encrypted with the passord swordfish, what must you do before you can obtain Page objects from it?
'''
First we must decrypt the PDF file with PdfFileReaderObj.decrypt('swordfish')
'''
# 6. What methods do you use to rotate a page?
'''
We have two methods for page objects, they are;
rotateClockwise() and rotateCounterClockwise(), then we pass the int value for 90,180,270
'''
# 7. What method returns a Document object for a file named demo.docx?
'''
doc = docx.Document('demo.docx') will return a Document object 
'''
# 8. What is the difference between a paragraph object and a Run object?
'''
Paragraph object is a group of Run objects, Paragraph object usually ends with when user enter the ENTER or RETURN key, and they don't end when style(color,boldness,italic,font etc..) ends. Whereas Run objects are smaller line in that paragraph, they end when the style changes.
'''
# 9. How do you obtain a list of Paragraph objects for a Document object that's stored in a variable named doc?
'''
doc.paragraphs will get all the paragraphs in a list from that document object. doc.paragraph[0] will get the first paragraph object in that document
'''
# 10. What type of object has bold,underline,italic,strike, and outline variables?
'''
Run object
'''
# 11. What is the difference between setting the bold variable to True,False or None?
'''
True ==> will always enable the bold
False ==> will always disables the bold
None ==> will set the default value of that run object
'''
# 12. How do you create a Document object for a new Word Document?
'''
doc.docx.Document(), will create a new blank word file document.
'''
# 13. How do you add a paragraph with the text 'Hello, there!' to a document object stored in a variable named doc?
'''
doc.add_paragraph('Hello, there!') will add the paragraph 'hello, there!' in to that document.
'''
# 14. What integers represent the levels of headings available in Word documents?
'''
0 to 4, 0 being the Title style, 1 to 4 is levels of headings 1 is being the biggest level and 4 is being the smallest(sub) level.
'''

## ------------- CHapter 16 : Working With CSV Files and JSON data ------------------------## 

# 1. What are some features Excel spreadsheets have that CSV spread-sheets don't?
'''
CSV files:
    * Don't have types for their values-- everything is a string
    * Don't have setting for font,size or color
    * Don't have multiple sheets
    * Can' specify cell widths and heights
    * Can't have merged cells
    * Can't have images or charts embedded in them
'''
# 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
'''
File Object as a result of the open() function 
'''
# 3. What modes do File objects for reader and writer objects need to be opened in?
'''
For Reader objects we don't need to specify a mode wheras for writer object file object needs to be open in a write('w') mode.
///
For reader objects they need to be opened in read-binary('rb') mode

For writer objects they need to be opened in write-binary('wb') mode
'''
# 4. What method takes a list argument and writes it to CSV file?
'''
writerow() method of Writer object
'''
# 5. What do the delimiter and lineterminator keyword arguments do?
'''
Delimiter ==> Character appears between cells in a row (By default it is comma)
lineterminator ==> Which character will appear at the end of the row (By default its the newline)
'''
# 6. What function takes a string of JSON data and returns a Python data structure?
'''
json.loads()
'''
# 7. What function takes a Python data structure and returns a string of JSON data?
'''
json.dumps()
'''
## ------------ Chapter 17: Keeping Time,Scheduling Tasks, and Launching Programs ---------##

# 1. What is the Unix epoch?
'''
Uni epoch is a time reference commonly used in programming. It is 12 am on January 1 , 1970 (UTC)
'''
# 2. What function returns the number of seconds since the Unix epoch?
'''
time.time()
'''
# 3. How can you pause your program fo exactly 5 seconds?
'''
time.sleep(5)
'''
# 4. What does the round() function return?
'''
Rounds the passed float value to the nearest integer. If we pass another integer value as a second argument that means how many digits after the decimal point will be included.
'''
# 5. What is the difference between a datetime object and a timedelta object?
'''
datetime is a specific moment in time while timedelta is a duration of time
'''
# 6. Using the datetime module, what day of the week was January 7,2019 ?
'''import datetime,time

date_time = datetime.datetime(2019,1,7,0,0,0)
print(date_time)
print(date_time.strftime('%A'))'''
'''
or use this;

datetime.datetime(2019,1,7).weekday() which returns 0. This means Monday
'''
# 7. Say you have a function named spam(). How can you call this function and run the code inside it in a seperate thread?
'''
subprocess.Popen(target=spam) and not subprocess.Popen(target=spam()) because the latter will take the function's return value instead of calling the code inside of it.
'''
# 8. What should you do to avoid concurrency issues with multiple threads?
'''
When you create a new Thread object make sure its function uses only local variables
'''

## Yeni branch'e atıldı
