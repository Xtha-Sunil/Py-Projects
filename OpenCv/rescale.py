import cv2 as cv

# big scale video has more information increasing the computational strain
# so we can resize or rescale to reduce workload to our computer
# generally its best practice to downscale the heiht and width coz most camera dont supporrt going higer than its maximium capability

def rescaleFrame(frame, scale=0.75):
    #works; for images , videos , live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension=(width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


#reading and resizing video
capture = cv.VideoCapture("assets/video/mb2.mp4")

while True:
    isTrue,frame = capture.read()

    resized_frame = rescaleFrame(frame,0.5)

    cv.imshow('video', frame)
    cv.imshow('video Resized', resized_frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
# cv2 error or -215 error is thrown either when  file is not found or after end of frame
capture.release()
cv.destroyAllWindows()