## Function for tablePrinter
## takes list of lists and displays in a well-organized table 
## 09/07/2021 Erim Serdönmez

tableData = [["apples","oranges","cherries","banana"],
["Alice","Bob","Carol","David"],
["dogs","cats","moose","goose"]]

### First Method
'''listlens = []
tour = 0
lists = {}
for m in tableData:
    total =0
    tour +=1
    for n in m:
        total + len(n)
        lists["list:",tour]= total
    print("lists",tour,total)

itemcount = list(lists.values())
sortedlen = (sorted(itemcount,reverse=True))
longest = sortedlen[0]

#print(lists['list:',1])
#print(longest)

for m in range(len(tableData[0])):
    for n in range(len(tableData)):
        print(tableData[n][m],end=" ")
        n+1
    print(" ".center(lists['list:',1]))
    m+1'''

## Second Method

'''# Empty dictionary for sorting the data
newTable = {0:[],1:[],2:[],3:[]}

# iterate through each list in tabledata
for li in tableData:
    for i in range(len(li)):
        # put each item of the table data inyo newtable by index
        newTable[i].append((li[i]))

# determine the longest list by number of total charactes
# for instance ['apples','Alice','dogs'] would be 15 characters
# we will start with longest being zero at the start
longest = 0
# iterate through newTable
# for example the first key:value will be 0:['apples','Alice','dogs']
# we only really care about the value ( the lists) in this case
for key,value in newTable.items():
    # determine the total characters in each list
    # so effectively len('applesAlicedogs') for the first list
    lenght = len(' '.join(value))
    # if the lenght is the longest lenght so far,
    # make that equal longest
    if lenght > longest:
        longest = lenght
# we will loop thorugh the newTable one last time
# printing spaces infront of each list equal to the difference
# between the lenght of the longest list and lenght of the current list
# this way its's al nice and tidy to the right
for key,value in newTable.items():
    print(' '* (longest - len(' '.join(value))) + ' '.join(value))'''

## Third Method


'''def printTable(mylist):
    # getting the item who has the max length in the inner tables
    maxLenghth = 0
    for item in mylist:
        for i in item:
            if len(i) > maxLenghth:
                maxLenghth = len(i)
            else:
                maxLenghth = maxLenghth
    # make a seperated rjust for every item in the inner lists
    for item in mylist:
        for i in range(len(item)):
            item[i] = (item[i].rjust(maxLenghth))
    # Convert list to dictionary data type it's more easier to deal with.
    myNewList = {0:[],1:[],2:[],3:[]}
    for i in range(len(item)):
        for u in tableData:
            myNewList[i].append(u[i])
    # print the output
    for key,value in myNewList.items():
        print(' '.join(value))


printTable(tableData)'''

## Forth Method

def table_printer(tab_data):
    col_widths = [0] * len(tab_data) # creates 3 lists based on the list lenght
    for j in range(len(tab_data[0])): # finds a length of 4 items (aka rows)
        for i in range(len(tab_data)): # find a lenght of 3 items ( aka columns)
            col_widths[i] = len((max(tab_data[i], key=len))) # sets the column width to the maximum lenght of an item in the list
            a = tab_data[i][j]
            print(a.rjust(col_widths[i]), end=" ") # every time we print a column, we rjust it to the max width
        print("\n")

table_printer(tableData)