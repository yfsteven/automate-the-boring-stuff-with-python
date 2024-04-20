#! python3
# insertBlankRows - read a workbook and insert M number of blank rows at row N
import openpyxl, sys
if len(sys.argv) == 4:
    wb = openpyxl.load_workbook(sys.argv[3])
    sheet = wb.active
    for i in range(int(sys.argv[2])):
        sheet.insert_rows(int(sys.argv[1]))
    wb.save(sys.argv[3])
