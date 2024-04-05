import cv2 as cv

def rescale(frame , scale = 0.5):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    new_dimn = (w,h)

    return cv.resize(frame,new_dimn, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("videos/1.mp4")


while True:
    isTrue, frame  = capture.read()
    resized = rescale(frame)

    cv.imshow("video", frame)
    cv.imshow("resized", resized) 

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()