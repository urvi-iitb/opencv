import cv2

img = cv2.imread("photos/1.jpg")
cv2.imshow("actual", img)

def rescaled(frame, scale = 0.5):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    new_dim = (width,height)

    return cv2.resize(frame, new_dim, interpolation = cv2.INTER_AREA)

img_resized = rescaled(img)

cv2.imshow("resized",img_resized)


cv2.waitKey(0)
cv2.destroyAllWindows()

