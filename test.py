import numpy as np
import cv2
import os
import cv2

file_array = []

def make_sequence(path, output_file):
    """Takes a series of images from a path and creates an mp4 with the output_file name"""
    for filename in os.listdir(path):
        if filename != '.DS_Store':
            file_array.append(filename)

    file_array.sort()

    img_array = []

    for file in file_array:
        img = cv2.imread(path + file)
        width, height = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 1, size)
    print('Number of images:', len(img_array))
    for i in enumerate(img_array):
        out.write(img_array[i])

def make_array(path):
    file_array = []
    img_array = []
    for filename in os.listdir(path):
        if filename != '.DS_Store':
            file_array.append(filename)

    file_array.sort()

    for file in file_array:
        img = cv2.imread(path + file)
        width, height, channels = img.shape
        size = (width, height)
        img_array.append(img)
    return img_array

image_array = make_array('./image_sequences/phone/')
print(image_array)
image_array = np.asarray(image_array)
med = np.median(image_array, axis=0)
image_array.append(med)
med = np.median(image_array)
cv2.imwrite('test2.jpg', med)