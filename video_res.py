#NOT TRIED YET AS IT CAN WORK ONLY WITH LIVE VIDEOS BEING READ FROM AN EXTERNAL CAMERA
#IT CANNOT BE USED FOR ALREADY EXISTING VIDEOS 

import cv2

capture = cv2.VideoCapture("videos/1.mp4")


def change_resolution(width, height):
    capture.set(3,height)
    capture.set(4,width)

while True:
    isTrue, frame  = capture.read()
    cv2.imshow("video", frame)
    
    if cv2.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()