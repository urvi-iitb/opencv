import cv2

capture = cv2.VideoCapture("videos/1.mp4")

while True:
    isTrue, frame = capture.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()