"""applies the median filtering algorithm to a series of images
    to eliminate unwanted moving artifacts"""
import os
import sys
import numpy as np
import cv2
from crop import crop

def get_files(path):
    """retrieves all the files needed for processing from the path"""
    file_array = []
    for filename in os.listdir(path):
        if filename != '.DS_Store':
            file_array.append(filename)

    file_array.sort()
    return file_array

def make_sequence(path, output_file):
    """make sequence creates a sequence of images"""
    file_array = get_files(path)

    img_array = []

    for file in file_array:
        img = cv2.imread(path + file)
        width, height, channels = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 1, size)
    print('Number of images:', len(img_array))
    for curr in img_array:
        out.write(curr)
    """for i in enumerate(img_array):
        out.write(img_array[i])"""

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
        #width, height, channels = img.shape
        #size = (width, height)
        img_array.append(img)
        
    return img_array

def align_image(original_path, aligned_path, original_file, transform_file, new_file):
    """aligns a given image"""
    original = cv2.imread(original_path + original_file)
    transform = cv2.imread(original_path + transform_file)

    original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    transform_gray = cv2.cvtColor(transform, cv2.COLOR_BGR2GRAY)

    size = original.shape

    warp_mode = cv2.MOTION_TRANSLATION # Translation not homography

    warp_matrix = np.eye(2, 3, dtype=np.float32)

    number_of_iterations = 5000
    termination_eps = 1e-10
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations, termination_eps)
    cc, warp_matrix = cv2.findTransformECC(original_gray, transform_gray, warp_matrix, warp_mode, criteria)

    transform_aligned = cv2.warpAffine(transform, warp_matrix, (size[1], size[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);
    cv2.imwrite(aligned_path + new_file, transform_aligned)
    print(aligned_path + new_file)


print(sys.argv[1]) # SEQUENCE PATH
print(sys.argv[2]) # ALIGNED PATH
print(sys.argv[3]) # OUTPUT NAME
print(sys.argv[4]) # POST PROCESSED OUTPUT NAME
print(sys.argv[5]) # BOOLEAN ALIGN

if(sys.argv[5] == "align=true"):
    align = True
else:
    align = False
print(sys.argv[5])
print(align)

## START IMAGE ALIGNMENT
file_array = get_files(sys.argv[1]) #all of the files we need

base_file = file_array[0]
counter = 1
if align is True:
    print('aligning...')
    for file in file_array: #align each file
        output = 'aligned_' + str(counter) + '.jpg'
        if file is not base_file: #the base file sets the standard for alignment
            align_image(sys.argv[1], sys.argv[2], base_file, file, output)
        else:
            original = cv2.imread(sys.argv[1] + base_file)
            print(sys.argv[2] + output)
            cv2.imwrite(sys.argv[2] + output, original)
        counter += 1

    image_array = make_array(sys.argv[2])
else:
    image_array = make_array(sys.argv[1])

med = np.median(image_array, axis=0)
cv2.imwrite(sys.argv[3], med)
## END IMAGE ALIGNMENT

# Removes the black bars bordering the image by cropping the image
if align is True:
    cropped = crop(sys.argv[3])
else:
    cropped = cv2.imread(sys.argv[3])
# Normalizes the pixel intensities in the image to produce a more appealing output
correct = cv2.normalize(cropped, None, alpha=50, beta=205, norm_type=cv2.NORM_MINMAX)
new_image = np.zeros(correct.shape, correct.dtype)
alpha = 1.8
beta = -50
for y in range(correct.shape[0]):
    for x in range(correct.shape[1]):
        for c in range(correct.shape[2]):
            new_image[y,x,c] = np.clip(alpha*correct[y,x,c] + beta, 0, 255)

#correct = cv2.addWeighted(correct, 30, np.zeros(correct.shape, correct.dtype), 0, 0)
cv2.imwrite(sys.argv[4], new_image)
