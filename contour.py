#CONTOUR DETECTION
import cv2 as cv
import numpy as np

img = cv.imread("photos/1.jpg")
blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
# blurring significantly reduces the number of contours found in the image
'''
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)
'''
canny = cv.Canny(img, 125,175)
cv.imshow("Canny", canny)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# threshold function is kind of binarizing the image, that is if the intensity is less than 125
# it sets it to 0 (black) and if greater than 125 then white (255)

contours, heirarchies= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #thresh
# 2nd argument is the mode ( either heirarchal, external or all contours)
#third is contour approximation argument , CHAIN_APPROX_SIMPLE is used to compress all the found contours into simpler ones
#contours is a python list of coordinates of all the found contours
#heirarchies contain the heirarchal representation of contours
print(len(contours))
cv.imshow("threshold", thresh)

#drawing the deteced contours on a blank image 
cv.drawContours(blank, contours, -1, (0,0,255), 1)
# -1 to specify all contours , it is basically the index
cv.imshow("drawn_contours", blank)

cv.waitKey(0)