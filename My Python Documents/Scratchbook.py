import csv,openpyxl,os

os.chdir('C:\\Users\\devil\\Desktop\\Project 16')

for filename in os.listdir('.'):
    if filename.endswith('_Sheet.csv'):
        os.unlink(filename)

