"""applies the median filtering algorithm to a series of images
    to eliminate unwanted moving artifacts"""
import os
import numpy as np
import cv2
from PIL import Image

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

    # where frame is a single image in a sequence
    for frame in file_array:
        img = cv2.imread(path + frame)
        blue, green, red = cv2.split(img)

        current_pixel = 0
        for column in blue:
            for pixel in column:
                #print(pixel)
                blue_channel_by_pixel[current_pixel].append(pixel)
                print(blue_channel_by_pixel[current_pixel])
                print("")
                current_pixel += 1
            print("zero")
            print(blue_channel_by_pixel[0])
            exit()

        print(current_pixel)    
        print("dont")
        print(blue_channel_by_pixel)
        exit()
        current_pixel = 0
        for column in green:
            for pixel in column:
                green_channel_by_pixel[current_pixel].append(pixel)
                current_pixel += 1

        current_pixel = 0
        for column in red:
            for pixel in column:
                red_channel_by_pixel[current_pixel].append(pixel)
                current_pixel += 1

    print("organized pixels")
    blue_medians = []
    for pixel in blue_channel_by_pixel:
        print(pixel)
        exit()
        pixel = np.sort(pixel)
        med = np.median(pixel, axis=0)
        blue_medians.append(med)

    print(blue_channel_by_pixel)
    exit()

    green_medians = []
    for pixel in green_channel_by_pixel:
        pixel = np.sort(pixel)
        med = np.median(pixel, axis=0)
        green_medians.append(med)

    red_medians = []
    for pixel in red_channel_by_pixel:
        pixel = np.sort(pixel)
        med = np.median(pixel, axis=0)
        red_medians.append(med)

    print("got medians")
    img_array = []
    img_array = cv2.merge((blue_medians, green_medians, red_medians))
    print("image array created")
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

    """# Show final results
    cv2.imshow("Image 1", original)
    cv2.imshow("Aligned Image 2", transform_aligned)
    cv2.waitKey(0)"""

## START IMAGE ALIGNMENT
file_array = get_files('./image_sequences/kirby/') #all of the files we need

base_file = file_array[0]
counter = 1
for file in file_array: #align each file
    output = 'aligned_' + str(counter) + '.jpg'
    if file is not base_file: #the base file sets the standard for alignment
        align_image('./image_sequences/kirby/', './image_sequences/aligned/kirby/', base_file, file, output)
    else:
        original = cv2.imread('./image_sequences/kirby/' + base_file)
        print('./image_sequences/aligned/kirby/' + output)
        cv2.imwrite('./image_sequences/aligned/kirby/' + output, original)
    counter += 1
image_array = make_array('./image_sequences/aligned/kirby/')
## END IMAGE ALIGNMENT

#image_array = make_array('./image_sequences/kirby/')
image_array = np.asarray(image_array)
med = np.median(image_array, axis=0)
cv2.imwrite('./results/kirby-euclidean-align.jpg', med)
