#! python3
# checkBeanCount.py - check every row to see if the total bean count is correct
import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
for i in range(2,15002):
    if int(ss[0].getRow(i)[0]) * int(ss[0].getRow(i)[1]) != int(ss[0].getRow(i)[2]):
        print('Row %s has an incorrect total count' % (i))
