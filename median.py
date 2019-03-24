"""applies the median filtering algorithm to a series of images
    to eliminate unwanted moving artifacts"""
import os
import numpy as np
import cv2
from PIL import Image

def make_sequence(path, output_file):
    """ NOTE: function is retired
    Takes a series of images from a path and creates an mp4 with the output_file name"""

    file_array = []
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
    """creates an image array based on a provided directory"""
    file_array = []
    img_array = []
    for filename in os.listdir(path):
        if filename != '.DS_Store':
            file_array.append(filename)

    file_array.sort()

    for file_name in file_array:
        img = cv2.imread(path + file_name)
        width, height, channels = img.shape
        size = (width, height)
        img_array.append(img)
    return img_array

def make_array_by_pixel(path):
    """creates an image array based on a provided directory"""
    file_array = []
    img_array = []
    for filename in os.listdir(path):
        if filename != '.DS_Store':
            file_array.append(filename)

    file_array.sort()

    temp = cv2.imread(path + file_array[0])
    num_pixels = temp.size

    blue_channel_by_pixel = [[]]*num_pixels
    green_channel_by_pixel = [[]]*num_pixels
    red_channel_by_pixel = [[]]*num_pixels

    for temp_file in file_array:
        img = cv2.imread(path + temp_file)
        blue, green, red = cv2.split(img)

        curr = 0
        for pixel in blue:
            blue_channel_by_pixel[curr].append(pixel)
            curr += 1

        curr = 0
        for pixel in green:
            green_channel_by_pixel[curr].append(pixel)
            curr += 1

        curr = 0
        for pixel in red:
            red_channel_by_pixel[curr].append(pixel)
            curr += 1

    blue_medians = []
    for pixel in blue_channel_by_pixel:
        med = np.median(pixel, axis=0)
        blue_medians.append(med)

    green_medians = []
    for pixel in green_channel_by_pixel:
        med = np.median(pixel, axis=0)
        green_medians.append(med)

    red_medians = []
    for pixel in red_channel_by_pixel:
        med = np.median(pixel, axis=0)
        red_medians.append(med)

    img_array = []
    curr = 0
    for pixel in blue_channel_by_pixel: #just need to go through ea. pixel
        img_array.extend(red_channel_by_pixel[curr])
        img_array.extend(blue_channel_by_pixel[curr])
        img_array.extend(green_channel_by_pixel[curr])

    return img_array

"""
NOTE: make_array_by_pixel currently throws a MemoryError cus she's TOO BIG
image_array = make_array_by_pixel('./image_sequences/phone/')
image_array = bytes(image_array)
final = Image.frombytes('RGB', (100, 360), image_array)
cv2.imwrite('test3.jpg', final)"""

image_array = make_array('./image_sequences/phone/')
# print(image_array)
image_array = np.asarray(image_array)
# image_array.sort(axis=0)
# ^ shouldn't we be sorting the values before getting the median?
med = np.median(image_array, axis=0)
image_array.append(med)
# ^ this is where i get an AttributeError: 'numpy.ndarray' object has no attribute 'append'
#   results in 'results' were computed when line 120 is commented out
# np.append(image_array, med, axis=0)
# ^ this is my attempt to fix it (doesn't work)
med = np.median(image_array)
cv2.imwrite('./results/test7.jpg', med)
