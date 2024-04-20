#! python3
# convertSpreadsheet.py - convert googlesheet to other format
import ezsheets
def convertSpreadsheet(ss):
    ss = ezsheets.upload(ss)
    ss.downloadAsExcel()
    ss.downloadAsODS()
    ss.downloadAsCSV()
    ss.downloadAsTSV()
    ss.downloadAsPDF()
    ss.downloadAsHTML()
