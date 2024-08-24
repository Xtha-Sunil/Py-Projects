#read images and vvideos using opencv

import cv2 as cv

#read image
img = cv.imread("assets/photo/img7.JPG")
cv.imshow("image", img)
cv.waitKey(0)

#read video
capture = cv.VideoCapture("assets/video/mb1.mp4")

while True:
    isTrue,frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
# cv2 error or -215 error is thrown either when  file is not found or after end of frame
capture.release()
cv.destroyAllWindows()
