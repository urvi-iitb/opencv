import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = "uint8")
blank[:] = 0,255,255  #BGR - 0 to 255

cv.putText(blank, "HELLO", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 10)
#after font type is the scale, color and thickness 
cv.imshow("Text",blank)
cv.waitKey(0)