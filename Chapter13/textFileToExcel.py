#! python3
# textFileToExcel.py - A function that inserts each line to all columns of a row
from pathlib import Path
import os, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

def textFileToExcel(file, rowNum):
    p = open(Path.cwd() / Path(f'{file}.txt'))
    lines = p.readlines()
    i = 0
    for line in lines:
        i += 1
        sheet.cell(row=rowNum,column=i).value = line.strip()
    wb.save('updated%s.xlsx' % (file))


