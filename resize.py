"""simple script to resize images"""
import os
import cv2

PATH = "./image_sequences/kirby/"
FILE_ARRAY = []
for filename in os.listdir(PATH):
    if filename != '.DS_Store':
        FILE_ARRAY.append(filename)
scale_percent = 25 # percent of original size

for file_name in FILE_ARRAY:
    img = cv2.imread(PATH + file_name)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, cv2.INTER_AREA)
    cv2.imwrite(PATH + file_name, resized)
