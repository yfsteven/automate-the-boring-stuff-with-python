#! python3
# deleteBulkyStuff.py
# Enter a folder and it will through the entire directory to look file or folder to delete
# based on its size
import os, shutil

def deleteBulkyStuff(folder):
    folder = os.path.abspath(folder)
    for folderName, subfolders, filenames in os.walk(folder):
        for subfolder in subfolders:
            if os.path.getsize(os.path.join(folderName, subfolder)) > 100000:
                print('Deleting subdirectory at ' + str(os.path.join(folderName, subfolder)))
                shutil.rmtree(os.path.join(folderName, subfolder))
        for filename in filenames:
            if os.path.getsize(os.path.join(folderName, filename)) > 10:
                print('Deleting file at ' + str(os.path.join(folderName, filename)))
                os.unlink(os.path.join(folderName, filename))


deleteBulkyStuff('cats')
