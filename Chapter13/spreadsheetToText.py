#! python3
# spreadsheetToText.py - a program that dots down every cells from each column to their respective text file
from pathlib import Path
import os, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

def spreadsheetToText(workbook):
    name = workbook
    workbook = openpyxl.load_workbook(Path.cwd() / Path(f'{workbook}.xlsx'))
    excel_sheet = workbook.active
    rowMax = excel_sheet.max_row
    columnMax = excel_sheet.max_column
    for i in range(columnMax):
        text_file = open(str(name) + 'stextfile' + str(i+1)+ '.txt', 'w')
        for k in range(rowMax):
            text_file.write(str(excel_sheet.cell(row=k+1,column=i+1).value) + '\n')
        text_file.close()
