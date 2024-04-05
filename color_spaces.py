#switching between colour spaces 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#OUTSIDE OPENCV THE DEFAULT COLOR SPACE IS RGB WHICH IS THE INVERSE OF BGR, DEFAULT IN OPENCV
# thus an inversion of colours takes place if u use , say matplotlib for the image

def resize(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    new_size = (width, height)
    return cv.resize(frame, new_size, interpolation=cv.INTER_AREA)

img = cv.imread("photos/2.jpg")
img = resize(img)
cv.imshow("original", img)
#hsv -s hue saturation value 
#it is more natural as it is related to the way humans percieve images 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow("HSV", hsv)


lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow("LAB", lab)

plt.imshow(img)
plt.show()

cv.waitKey(0)