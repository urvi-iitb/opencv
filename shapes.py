import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype="uint8")  #uint8 is for image datatype
# WE give the height , width and the number of colour channels in the size of the np array 

blank[:] = 0,0,0         # Blue, green, red
#cv.imshow("blank",blank)

# blank[200:300,200:300]=0,0,255
# cv.imshow("diff", blank)

#cv.rectangle(blank, (0,0), (250,250), (0,255,255), thickness = 2)
#if thickness = -1 or cv.FILLED then it fills the entire shape otherwise it is the line thickness

cv.rectangle(blank,(0,0),((blank.shape[0])//2, blank.shape[1]//2),(0,255,0),thickness = cv.FILLED)
#similarly cv.line for drawing a line 

cv.imshow("rect", blank)

cv.circle(blank, ((blank.shape[1])//2, (blank.shape[0])//2),40,(0,0,255), thickness = -1)
#image, center, radius, color and thickness 

cv.imshow("circle", blank)


cv.waitKey(0)
