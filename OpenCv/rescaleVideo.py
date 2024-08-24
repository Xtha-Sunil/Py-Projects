import cv2 as cv

def changeRes(width, height):
    # 3 refrence width , 4 for height, 10 for brightness
    # works for liv video only i.e reading from external camera
    capture.set(3,width)
    capture.set(4,height)


#reading and resizing video
capture = cv.VideoCapture(0)
# dont call inside loop
changeRes(300, 500)

while True:      
    isTrue,frame = capture.read()

    cv.imshow('stream 0', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# cv2 error or -215 error is thrown either when  file is not found or after end of frame
capture.release()
cv.destroyAllWindows()