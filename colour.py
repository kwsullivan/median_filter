"""implementing colour correction for the resulting images"""
import cv2
from matplotlib import pyplot as plt

def colour_correction(img):
    """corrects the colour of an image"""
    #img = cv2.imread(src)
    img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    new = cv2.normalize(img, None, alpha=50, beta=255, norm_type=cv2.NORM_MINMAX)
    new_hist = cv2.calcHist([new], [0], None, [256], [0, 256])
    cv2.imwrite('./results/colour_corrected_kirby_4.jpg', new)
