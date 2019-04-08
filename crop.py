import cv2
import numpy as np

def crop(image_name):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)


    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    
    x, y, w, h = cv2.boundingRect(cnt)
    cropped = image[y:y+h-1, x:x+w-1]

    return cropped

image = cv2.imread('./image_sequences/aligned/aligned.jpg')
cropped = crop(image)
cv2.imwrite('cropped.jpg', cropped)