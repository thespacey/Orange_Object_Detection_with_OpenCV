from __future__ import division
import sys
import cv2
#to show the image
from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin

green = (0, 255, 0)

def show(image):
    # Figure size in inches
    plt.figure(figsize=(10, 10))

    # Show image, with nearest neighbour interpolation 
    plt.imshow(image, interpolation='nearest')

def overlay_mask(mask, image):
    #make the mask rgb
     rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
     #calculates the weightes sum of two arrays. in our case image arrays
     #input, how much to weight each. 
     #optional depth value set to 0 no need
     img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
     return img

def find_biggest_contour(image):
    # Copy
    image = image.copy()
    #input, gives all the contours, contour approximation compresses horizontal, 
    #vertical, and diagonal segments and leaves only their end points. For example, 
    #an up-right rectangular contour is encoded with 4 points.
    #Optional output vector, containing information about the image topology. 
    #It has as many elements as the number of contours.
    #we dont need it
    image, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Isolate largest contour
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    return biggest_contour, mask

def circle_contour(image, contour):
    # Bounding ellipse
    image_with_ellipse = image.copy()
    #easy function
    ellipse = cv2.fitEllipse(contour)
    #add it
    cv2.ellipse(image_with_ellipse, ellipse, green, 2, cv2.LINE_AA)
    return image_with_ellipse

def find_orange(image):
    #RGB stands for Red Green Blue. Most often, an RGB color is stored 
    #in a structure or unsigned integer with Blue occupying the least 
    #significant “area” (a byte in 32-bit and 24-bit formats), Green the 
    #second least, and Red the third least. BGR is the same, except the 
    #order of areas is reversed. Red occupies the least significant area,
    # Green the second (still), and Blue the third.
    # we'll be manipulating pixels directly
    #most compatible for the transofrmations we're about to do
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Make a consistent size
    #get largest dimension
    max_dimension = max(image.shape)
    #The maximum window size is 700 by 660 pixels. make it fit in that
    scale = 700/max_dimension
    #resize it. same width and hieght none since output is 'image'.
    image = cv2.resize(image, None, fx=scale, fy=scale)

    #we want to eliminate noise from our image. clean. smooth colors without
    #dots
    # Blurs an image using a Gaussian filter. input, kernel size, how much to filter, empty)
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    
    image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)
    min_ora = np.array([10, 50, 50])
    max_ora = np.array([30, 255, 255])
    mask1 = cv2.inRange(image_blur_hsv, min_ora, max_ora)
    min_ora2 = np.array([170, 50, 50])
    max_ora2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(image_blur_hsv, min_ora2, max_ora2)
    mask = mask1 + mask2

    # Clean up
    #we want to circle our orange so we'll circle it with an ellipse
    #with a shape of 15x15
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel)
    big_orange_contour, mask_oranges = find_biggest_contour(mask_clean)
    overlay = overlay_mask(mask_clean, image)
    circled = circle_contour(overlay, big_orange_contour)
    show(circled)
    bgr = cv2.cvtColor(circled, cv2.COLOR_RGB2BGR)
    return bgr
image = cv2.imread(r'C:\Users\MARSYAS\Desktop\o.jpg')
result = find_orange(image)
cv2.imwrite(r'C:\Users\MARSYAS\Desktop\o2.jpg', result)
