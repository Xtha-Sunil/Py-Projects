import cv2 as cv
import numpy as np
import math

blank = np.zeros((500,500,3),dtype="uint8")
frames = 100
center=(250,250)
radius = 50

for i in range(frames):
    angle = i*(360/frames)
    angle_rad = math.radians(angle)
    end = (int(center[0] + radius * math.cos(angle_rad)), int(center[1] + radius * math.sin(angle_rad)))
    cv.line(blank, center,end, (0,255,0),3)
    cv.imshow("circle", blank)
    cv.waitKey(20)

cv.waitKey(0)
cv.destroyAllWindows()