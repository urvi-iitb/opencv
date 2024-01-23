import cv2 as cv
import numpy as np

#TRANSLATION ( shifting along x and y axes )

#x and y denote the number of pixels in x ad y direction to be shifted 
def translate(img, x, y):
    # transformation matrix
    mat = np.float32(([1,0,x],[0,1,y]))
    dim = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, mat, dim)

# -ve x -> left
# +ve x -> right
# -ve y -> up
# +ve y -> down

img = cv.imread("photos/1.jpg")

'''
translated = translate(img, 100, 100)  # shifted down and right 
cv.imshow("translated", translated)
'''

#ROTATION BY SOME ANGLE
# u can take any arbitrary point as the center of rotation

def rotate(img, angle, rotPoint= None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotation_mat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #last argument is for scaling the image
    dim = (width,height)

    return cv.warpAffine(img, rotation_mat, dim)

'''
rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)
'''

#FLIPPING AN IMAGE
flipped = cv.flip(img, -1) # 0 means along x axis, 1 along y axis and -1 along both
cv.imshow("flipped", flipped)

cv.waitKey(0)