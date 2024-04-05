import cv2 as cv

def resize(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    new_size = (width, height)

    #resizes ignoring the aspect ratio
    return cv.resize(frame, new_size, interpolation=cv.INTER_AREA) #INTER_AREA to fit image when we shrink it 
    #INTER_LINEAR or INTER_CUBIC if u want to enlarge


img  = cv.imread("photos/2.jpg")
img = resize(img)
cv.imshow("Original", img)

#GRAYSCALE IMAGE
# converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blurring an image 
#used to remove noise from the image 

blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)


#(3,3) is the kernel size which is directly a measure of how much to blur 
#so to increase the blur u can give like (5,5), it always has to be odd

#edge cascade 
#canny edge cascade is one type 

canny = cv.Canny(blur, 125,175)
cv.imshow("canny_edges", canny)

#125, 175 are the lower and upper bounds on the intensity gradient based on which it is decided whether
# a pixel is a part of an edge or not 
#u can reduce the number of edges detected by blurring the image appropriately



#DILATING AN IMAGE 
#(3,3) is the kernel size and using canny image for edges dilation 

dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow("Dilated", dilated )



#getting back the original image if it is dilated
''' 
eroded = cv.erode(dilated, (7,7), iterations = 10)
cv.imshow("eroded", eroded)
'''

#CROPPING IMAGES 

cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)