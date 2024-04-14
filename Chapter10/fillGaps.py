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
    file_data = {}
    prefix = ''
    pre = ''
    listo = []
    for file in os.listdir(folder):
        mo = prefixPattern.search(file)
        if mo == None:
            continue
        prefix = mo.group(1) + mo.group(2) + mo.group(3)
        pre = mo.group(1)
        file_data[mo.group(1)] = int(mo.group(2))
        listo.append(int(mo.group(2)))
    if len(file_data) > 0:
        largest_value = max(listo)
        for i in range(largest_value):
            k = i + 1
            if k not in listo:
                if k < 10:
                    shutil.copy(os.path.join(folder, prefix), pre + '00' + str(i+1))
                if k >= 10 and k < 100:
                    shutil.copy(os.path.join(folder, prefix), pre + '0' + str(i+1))
                if k >= 100:
                    shutil.copy(os.path.join(folder, prefix), pre + str(i+1))


fill_gaps('')

