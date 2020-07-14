import cv2
import numpy as np
import matplotlib
import sys
import os
import fnmatch

def sharpen(image):
    kernel = np.array([[0, -1, 0], [1, 5, -1],[0, -1,0]])
    new_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow('Sharpened Image', new_image)
    cv2.waitKey(0)
    return new_image


def resize(fname, width, height):
    image = cv2.imread
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    org_height, org_width = image.shape[0:2]
    print('Height: ', org_height)
    print('Width: ', org_width)

    if org_width >= org_height:
        new_image = cv2.resize(image,(width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    return fname, new_image

def blur(image):
    kernels = [3, 5, 9, 12]
    for idx, k in enumerate(kernels):
        image_bl = cv2.blur(image, ksize = (k,k))
        cv2.imshow(str(k), image_bl)
        cv2.waitKey(0)


listofFiles = os.listdir('.')
pattern = '*.jpg'
n = len(sys.argv)
if n == 3:
    width = int(sys.afgv[1])
    height = int(sys.argv[2])
else:
    width = 1280
    height = 960
if not os.path.exists('new_folder'):
    os.makedirs('new_folder')

for filename in listofFiles:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_image= resize(filename,width, height)
        cv2.imwrite('new_folder\\' + filename, new_image)
#cv2.imshow('Resized Image', new_image)
#cv.waitKey(0)
#blur(new_image)
#image = sharpen(new_image)
