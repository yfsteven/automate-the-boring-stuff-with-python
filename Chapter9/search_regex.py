#! python3
# search_regex.py - Search all text files to look for specific regular expression. If it does, it gives back the line that contains the expression and the file.
from pathlib import Path

get_input = input('What do you want to find? \n')

for textFilePathObj in p.glob('*.txt'):
    file = open(textFilePathObj)
    content = file.readlines()
    for line in content:
        if get_input in line:
            print(line, textFilePathObj)


