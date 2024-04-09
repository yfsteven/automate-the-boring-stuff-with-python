#! python3
# regexStrip

import re

def regex_strip(text, char=''):
    regex = re.sub(r'^\s+|\s+$', char, text)
    return(regex)

