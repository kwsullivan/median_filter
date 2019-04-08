import cv2
import numpy as np

def compare_diff(truth_name, image_name):
    truth = cv2.imread(truth_name)
    image = cv2.imread(image_name)
    difference = cv2.subtract(truth, image)
    b, g, r = cv2.split(difference)
    print('B:', b)
    print('G:', g)
    print('R:', r)
