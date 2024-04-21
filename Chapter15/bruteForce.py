#! python3
# bruteForce.py - a program that bruteforce encrypted pdf file using a list containing 40,000 single words
import PyPDF2
from pathlib import Path

p = open(Path.cwd() / 'dictionary.txt')
lines = p.readlines()

minutesFile = open('encryptedmeetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(minutesFile)

password = 'Nothing'

for line in lines:
    line = line.strip('\n')
    if pdf_reader.decrypt(line) == 2:
        password = line.strip().lower()
        break
    if pdf_reader.decrypt(line.lower()) == 2:
        password = line.strip().lower()
        break
print(password)
