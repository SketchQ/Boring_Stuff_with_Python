#! python3

## PROJECT: Combining Select Pages from Many PDFs

    # Say you have the boring job of merging several dozen PDF documents into a single PDF file. Each of them has a cover sheet as the first page, but you don’t want the cover sheet repeated in the final result. Even though there are lots of free programs for combining PDFs, many of them simply merge entire files together. Let’s write a Python program to customize which pages you want in the combined PDF.


## The Program will do :
    # 1. Find all PDF Files in the current working Directory
    # 2. Sort the filenames so the PDFs are added in order.
    # 3. Write each page, excluding the first page, of each PDF to the output file.

## Your Code needs to the following:
    # 1. Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
    # 2. Call Python's sort() list method to alphabetize the filenames.
    # 3. Create a PdfFileWriter object for the output PDF.
    # 4. Loop over each PDF file, creating a PdfFileReader object for it.
    # 5. Loop over each page(except the first) in each PDF file.
    # 6. Add the pages to the output PDF.
    # 7. Write the output PDF to a file named allminutes.pdf.

## STEP 1: Find all PDF Files
## STEP 2: Open Each PDF
## STEP 3: Add Each Page
## STEP 4: Save the Results


#! python3
# combinepdfs.py -- Combines all the PDFs in the current working directory into a single PDF.

import PyPDF2,os

from PyPDF2.utils import PdfReadError

os.chdir('C:\\Users\\devil\\Desktop\\Python Beginners Code and Basics\\Automate the boring staff with Python\Files used in the book\\Automate_the_Boring_Stuff_2e_onlinematerials\\automate_online-materials')

# Get all the PDF filenames.
pdfFiles = []

# The os.list('.') call will return a list of every file in the cwd. The code loops over this list and adds only those files with the .pdf extension to pdfFiles list.
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# This list is sorted in alphabetical order with the key=str.lower
pdfFiles.sort(key=str.lower)

# Writer object is created to hold the combined PDF pages.
pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop Through all the PDF files.

# For every file in the pdfFiles list we create a new file object with open(), then we turn those file objects into a Reader object.
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # TODO: Loop through all the pages(except the first) and add them.

    # This code copies each Page object into a Writer object.Becouse PyPDF2 considers 0 as the first page we start at 1 and continue with the reader.numPages
    try:
        for pageNum in range(1,pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    except PdfReadError:
        continue
# TODO: Save the resulting PDF to a file.

pdfOutput = open('allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

## Ideas for similar Programs:
    # Cut out specific pages from PDFs.
    # Reorder pages in a PDF.
    # Create a PDF from only those pages that have some specific text, identified by extractText().