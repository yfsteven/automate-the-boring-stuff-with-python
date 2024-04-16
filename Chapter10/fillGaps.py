#! python3
# fillGaps.py - Duplicate all necessary files enough to insert inside the gap
import shutil, os, re

prefixPattern = re.compile(r"""
    ^(digit)
    (\d{3})
    (.*?)$
    """, re.VERBOSE)

def fill_gaps(folder):
    folder = os.path.abspath(folder)
    i = 1
    for file in os.listdir():
        mo = prefix_regex.search(file)
        if mo:
            old_name = os.path.abspath(file)
            new_suffix = mo.group(1) + str(i).zfill(3) + '.jpg'
            new_name = os.path.join(path, new_suffix)
            i += 1
            print('Renaming: %s to %s' % (old_name, new_name))
            shutil.move(old_name, new_name)


fill_gaps('')

