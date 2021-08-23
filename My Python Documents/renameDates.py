#! python 3
# Here’s what the program does:

# It searches all the filenames in the current working directory for American-style dates.
# When one is found, it renames the file with the month and day swapped to make it European-style.

# Code will do the following

# Create a regex that can identify the text pattern of American-style dates.
# Call os.listdir() to find all the files in the working directory.
# Loop over each filename, using the regex to check whether it has a date.
# If it has a date, rename the file with shutil.move().

## Step 1: Create a Regex for American-Style Dates


import re,shutil,os

# Create a regex for the matches file with the American date format

datePattern = re.compile(r"""^(.*?) # All text before the date
((0|1)?\d)-                         # one or two digits for the month
((0|1|2|3)?\d)-                     # one or two digits for the day
((19|20)\d\d)                       # four digits for the year
(.*?)$                              # all text after the date
""",re.VERBOSE)

# : Loop over the files in the cwd.7

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# : Skip files without date.

    if mo == None:
        continue

# : Get the different parts of the filename.

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    daypart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# : Form the European-style filename.
    euroFilename = beforePart+daypart+'-'+monthPart+'-'+yearPart+afterPart


# : Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

#: Rename the files.
    print(f'Remaining "{amerFilename}" to "{euroFilename}"...')
   #shutil.move(amerFilename,euroFilename) # Uncomment after testing

## Step 2: Identify the Date parts from the filenames

# Next, the program will have to loop over the list of filename strings returned from os.listdir() and match them against the regex. Any files that do not have a date in them should be skipped. For filenames that have a date, the matched text will be stored in several variables. 

## Step 3: Form the new Filename and Rename the Files.

# As the final step, concatenate the strings in the variables made in the previous step with the European-style date: the date comes before the month.