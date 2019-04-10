import cv2
import numpy as np
import sys

def compare_diff(truth_name, image_name, threshold):
    truth = cv2.imread(truth_name)
    image = cv2.imread(image_name)
    diff = cv2.absdiff(image, truth)
    ret, thresh = cv2.threshold(diff, int(threshold), 255, cv2.THRESH_BINARY)
    """cv2.imshow('thresh', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
    black_pixels = np.sum(thresh == 0) / 3
    
    width, height, channels = diff.shape
    size = width * height
    print(int(black_pixels), '/', size, '(black pixels / total pixels)')
    return (black_pixels / size) * 100

index = compare_diff(sys.argv[1], sys.argv[2], sys.argv[3])
print("SCORE: {}%".format(round(index, 3)))