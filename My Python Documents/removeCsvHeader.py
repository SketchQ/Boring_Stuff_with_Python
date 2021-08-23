#! python3
# removeCsvHeader.py -- Removes the header from all CSV files in the current working directory

## STEP 1: Loop through each CSV file
## STEP 2: Read in the CSV file
## STEP 3: Write out the CSV file Without the first row
import csv,os

os.chdir('C:\\Users\\devil\\Desktop\\Python Beginners Code and Basics\\Automate the boring staff with Python\Files used in the book\\Automate_the_Boring_Stuff_2e_onlinematerials\\automate_online-materials')

os.makedirs('headerRemoved',exist_ok=True)

# Loop through every file in the current working directory.

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue                            # Skip the non-csv files
    print('Removing header from ' + csvFilename + '...')

    # TODO : Read the CSV file in (Skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue                        # Skip the first row
        csvRows.append(row)
    csvFileObj.close()
    # TODO : Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved',csvFilename),'w',newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

## Ideas for Similar programs:

    # Compare data between different rows in a CSV file or between multiple CSV files.
    # Copy specific data from CSV file to an Excel file, or vice versa.
    # Check for invalid data or formatting mistakes in CSV files and alert the user to these errors.
    # Read data from a CSV file as input for your Python programs.