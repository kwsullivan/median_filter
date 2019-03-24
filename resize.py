"""simple script to resize images"""
import os
from PIL import Image

PATH = "./image_sequences/zoom/"

FILE_ARRAY = []
for filename in os.listdir(PATH):
    if filename != '.DS_Store':
        FILE_ARRAY.append(filename)

for file_name in FILE_ARRAY:
    img_file = Image.open(PATH + file_name)
    img = img_file.resize((270, 180), Image.ANTIALIAS)
    img.save(PATH + file_name, optimize=True, quality=85)
