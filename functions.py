import cv2 as cv

# converting an image to grayscale
def resize(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    new_size = (width, height)

    return cv.resize(frame, new_size, interpolation=cv.INTER_AREA)

img  = cv.imread("photos/2.jpg")
img = resize(img)
cv.imshow("Original", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)


# blurring an image 
#used to remove noise from the image 

blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
#(3,3) is the kernel size which is directly a measure of how much to blur 
#so to increase the blur u can give like (5,5), it always has to be odd

cv.imshow("Blurred", blur)


cv.waitKey(0)