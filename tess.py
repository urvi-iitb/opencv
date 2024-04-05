import pytesseract as ts
import cv2 as cv
from PIL import Image

#img = Image.open('photos/angled.jpg')
config = r"--psm 10 --oem 3"

def rescaled(frame, scale = 0.5):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    new_dim = (width,height)
    return cv.resize(frame, new_dim, interpolation = cv.INTER_AREA)


img = cv.imread("photos/board.jpg")
img = rescaled(img)
ht,wd,_ = img.shape
boxes = ts.image_to_boxes(img,config = config)
#print(boxes)
for box in boxes.splitlines():
    box = box.split(" ")

img = cv.rectangle(img, (int(box[1]), ht - int(box[2]),int(box[3]), ht - int(box[4])), (0,255,0),2)

cv.imshow("img",img)
cv.waitKey(0)
#ts.pytesseract.tesseract_cmd = r'/bin/tesseract'
#print(ts.image_to_string(img, config=config))