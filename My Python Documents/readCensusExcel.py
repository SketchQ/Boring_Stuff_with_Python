#! python3
# readCensusExcel.py- counts both population and number of census tracts for each county

## This is what this program will do:
    # 1.Reads the data from the Excel Spreadsheet
    # 2.Counts the number of census tracts in each county
    # 3.Count the total population of each county
    # 4.Print the results.

## Code will do the following:
    # 1.Open and read the cells of an Excel document with the openpyxl module.
    # 2.calculate all the tract and population data and store it in a data structure.
    # 3.Write the data structure to a text file with the .py extension using the pprint module.

## Step 1 : Read the Spreadsheet Data


from os import stat
import openpyxl,pprint      # import openpyxl module as well as the pprint module

print('Opening Workbook...\n')
wb = openpyxl.load_workbook('censuspopdata.xlsx')   # Opens up the censuspopdata.xlsx file
sheet = wb['Population by Census Tract']            # Gets the sheet from the workbook
countyData = {}                                     # this will contain the populations and  number of tracts we calculate for each county. Before we can store anything in it, though you should determine exactly how you'll structure the data inside it.

## Step 2: Populate the data structure

# the data structure in countyData will be a dictionary with state abbreviations (AL) as its keys.
# Each state abbreviation will map to another dictionary, whose keys are strings of the county names in that state.
# Each county name will in turn map to a dictionary with just two keys 'tracts' and 'pop'
# These keys map to the number of census tracts and population for the county

# Example :
'''
        {'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1},
        'Aleutians West': {'pop': 5561, 'tracts': 2},
        'Anchorage': {'pop': 291826, 'tracts': 55},
        'Bethel': {'pop': 17013, 'tracts': 3},
        'Bristol Bay': {'pop': 997, 'tracts': 1},
        --snip-- 
'''
# These will evaluate to below:
'''      countyData['AK']['Anchorage']['pop']
         >>> 291826
         countyData['AK']['Anchorage']['tracts']
         >>> 55     
'''
# More generally the countyData will look like this:
'''
countyData[state abbrev][county]['tracts']
countyData[state abbrev][county]['pop']
'''

#  Fill in countyData with each county's population and tracts.
print('Reading rows...\n')
for row in range(2,sheet.max_row+1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state,{})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county,{'tracts':0,'pop':0})
    
    # Each row represents one censuc tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

## Step 3: Write the Results to a File


# Open a new text file and write the contents of countyData to it.
print('Writing Results...\n')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' +pprint.pformat(countyData))
resultFile.close()
print('Done.')

# import the file we've written our data in

import os


