#! python3
# dateDetection.py Detects dates in the DD/MM/YYYY format
import re, pyperclip

dates_box = re.compile(r'''(
            (\d{1,2}) #Days
            \/
            (\d{1,2}) #Months
            \/
            (\d{1,4}) #Years
            )''', re.VERBOSE)

mo = dates_box.findall(str(pyperclip.paste()))

#str(pyperclip.paste())

month = []
day = []
year = []

if len(mo) > 0:
    for i in range(len(mo)):
        if len(mo[i][2]) == 1 and len(mo[i][2]) < 2:
            month.append('0' + mo[i][2])
        if len(mo[i][1]) == 1 and len(mo[i][1]) < 2:
            day.append('0' + mo[i][1])
        if len(mo[i][2]) > 1:
            month.append(mo[i][2])
        if len(mo[i][1]) > 1:
            day.append(mo[i][1])
        year.append(mo[i][3])
else:
    print('No dates')

combined_list = [day, month, year]

def date_validator(d):
    date_list = d.split('/')
    thirty_days = ['04','06','09','11']
    for i in date_list:
        if int(i) == 0:
            return d + ' is an invalid date'
    if int(date_list[2]) < 1000 or int(date_list[2]) > 2999:
        return d + ' is an invalid date'
    if int(date_list[0]) > 31:
        return d + ' is an invalid date'
    if int(date_list[1]) > 12:
        return d + ' is an invalid date'
    if date_list[1] in thirty_days:
        if int(date_list[0]) <= 30:
            return d + ' is a valid date'
        else:
            return d + ' is an invalid date'
    if int(date_list[1]) == 2:
        if int(date_list[2]) % 4 == 0 and int(date_list[0]) <= 29 and not int(date_list[2]) % 100 == 0:
            return d + ' is a valid date'
        elif int(date_list[0]) <= 28:
            return d + ' is a valid date'
        else:
            return d + ' is an invalid date'
    return d + ' is a valid date'

for i in range(len(combined_list[0])):
    date = ''
    for k in range(len(combined_list)):
        if k == len(combined_list) - 1:
            date += combined_list[k][i]
        else:
            date += combined_list[k][i] + '/'
    print(date_validator(date))














