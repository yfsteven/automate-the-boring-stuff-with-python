#! python3
# selectiveCopy.py

import shutil, os, re
import pyinputplus as pyip

get_filextension = pyip.inputStr('Enter file extension: \n')
insert_folder = pyip.inputStr('Enter a source folder: \n')
insert_nfolder = pyip.inputStr('Enter a destination folder: \n')

def selectiveCopy(folder, nfolder, ext):
    folder = os.path.abspath(folder)
    nfolder = os.path.abspath(nfolder)
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(ext):
                shutil.move(os.path.join(folder, filename), nfolder)

selectiveCopy(insert_folder, insert_nfolder, get_filextension)
