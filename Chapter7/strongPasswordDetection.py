#! python3
# strongPasswordDetection.py

import re

"""
Write a function that uses regular expressions to make sure
the password string it is passed is strong. A strong password is
defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and
has at least one digit. You may need to test the
string against multiple regex patterns to validate its strength.
"""

def strong_password(p):
    passwordRegex = re.compile(r'''(
    ^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$
    )''', re.VERBOSE)
    test = passwordRegex.search(p)
    if test:
        print(p + ' is a strong password')
    else:
        print(p + ' is not a strong password')

strong_password(input('Enter a password \n'))
