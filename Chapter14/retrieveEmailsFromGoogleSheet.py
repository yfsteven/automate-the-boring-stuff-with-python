#! python3
# retrieveEmailsFromGoogleSheet.py - collects a list of the email addresses from google spreadsheet
import ezsheets
ss = ezsheets.Spreadsheet('') #Include your spreadsheet ID
sheet = ss.sheets[0]
emailColumn = sheet.getColumn(3) #Select the column that contains the list of email addresses
for email in list(dict.fromkeys(emailColumn).keys()):
    print('%s\n' % (email))
