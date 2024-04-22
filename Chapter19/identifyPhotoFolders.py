#! python3
# identifyPhotoFolders.py - look through every file and directory to identify photo folders
import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/home'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename
        # Open image file using Pillow.
        im = Image.open(os.path.join(foldername, filename))
        width, height = im.size

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    totalCount = numNonPhotoFiles + numPhotoFiles
    if totalCount != 0:
        if numPhotoFiles / totalCount >= 0.50:
            print(foldername)

