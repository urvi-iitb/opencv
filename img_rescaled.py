import cv2 as cv

img = cv.imread("photos/2.jpg")
cv.imshow("actual", img)

def rescaled(frame, scale = 0.5):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    new_dim = (width,height)
    return cv.resize(frame, new_dim, interpolation = cv.INTER_AREA)

img_resized = rescaled(img)

cv.imshow("resized",img_resized)

cv.waitKey(0)
cv.destroyAllWindows()
