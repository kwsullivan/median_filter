import cv2
import numpy as np
import sys

def crop(image):
    print('cropping...')
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    print(image.shape)
    
    x, y, w, h = cv2.boundingRect(cnt)
    print(x, y, w, h)

    print(x, x+w-1)
    print(y, y+h-1)

    cropped = image[y:y+h+5, x:x+w+5]

    return cropped

 # Removes the black bars bordering the image by cropping the image
cropped = crop(sys.argv[1])
# Normalizes the pixel intensities in the image to produce a more appealing output
correct = cv2.normalize(cropped, None, alpha=50, beta=205, norm_type=cv2.NORM_MINMAX)
"""new_image = np.zeros(correct.shape, correct.dtype)
alpha = 1.8
beta = -50
for y in range(correct.shape[0]):
    for x in range(correct.shape[1]):
        for c in range(correct.shape[2]):
            new_image[y,x,c] = np.clip(alpha*correct[y,x,c] + beta, 0, 255)"""

#correct = cv2.addWeighted(correct, 30, np.zeros(correct.shape, correct.dtype), 0, 0)
cv2.imwrite(sys.argv[2], cropped)