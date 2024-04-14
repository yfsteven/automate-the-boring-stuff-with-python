# Write your code here :-)
from pathlib import Path
import pyinputplus as pyip
import os
import re

def madLib(file):
    p = Path.cwd() / Path(f'{file}.txt')
    saved_text = p.read_text()
    regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    find_words = regex.findall(saved_text)
    if len(find_words) > 0:
        for i in range(len(find_words)):
            if find_words[i].lower() == 'adjective' or find_words[i].lower() == 'adverb':
                get_inputs = pyip.inputStr(f'Enter an {find_words[i].lower()}: \n')
                saved_text = regex.sub(get_inputs, saved_text, 1)
            else:
                get_inputs = pyip.inputStr(f'Enter a {find_words[i].lower()}: \n')
                saved_text = regex.sub(get_inputs, saved_text, 1)
        new_file = open(f'madlib_{file}.txt', 'w')
        new_file.write(saved_text)
        print(f'New file has been created. Named madlib_{file}.txt.')
    else:
        print('Nothing has been madlibbed')
