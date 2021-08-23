import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']

for i in range(5,101):
    sheet.row_dimensions[i] = 200

wb.save('trying.xlsx')