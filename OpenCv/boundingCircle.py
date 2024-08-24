import cv2 as cv
import numpy as np
import math

r1,x1,y1,r2,x2,y2=80,400,250,50,400,350

if r1 > r2:
    r1, r2 = r2, r1

blank = np.zeros((650,1000,3), dtype="uint8")

#calculate the bounding circle
dis = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))

if dis+r1<=r2:
    r,center = r2,(x2,y2)
else:
    r = round((dis+r1+r2)/2)+1
    theta = 0.5 + (r2-r1)/(2*dis)
    center = (round((1-theta)*x1 + theta*x2), round((1-theta)*y1 + theta*y2))

for radius in range(r2+1):
    blank.fill(0)
    cv.circle(blank, (x2,y2), radius, (255,0,0), 2)
    cv.circle(blank, (x1,y1), min(r1, radius), (255,255,255), 2)
    cv.imshow("Bounding circle", blank)
    cv.waitKey(20)

frames = 400
for i in range(frames+1):
    angle = i * (360/frames)
    angle_rad = math.radians(angle)
    end = (int(center[0] + r * math.cos(angle_rad)), int(center[1] + r * math.sin(angle_rad)))
    cv.line(blank, end, end , (0,0,255), 3)
    cv.imshow("Bounding circle", blank)
    cv.waitKey(1)

cv.waitKey(0)
cv.destroyAllWindows()