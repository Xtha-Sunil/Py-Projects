import cv2 as cv
import numpy as np


# height, width, color channel , dtype = image
blank = np.zeros((500,500,3), dtype="uint8")

#blank[100:200, 250:400] = 0,255,0
cv.imshow('Blank', blank)

#rectangle
#image, topLeftcorner, bottomRightCorner, color in BGR, thickness (-1 is fill)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#circle
#image, center , radius, color in BGR, thickness
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED)
cv.imshow('Circle', blank)

#line
#image, start, end, colour , thicknaess
cv.line(blank,(0,0) ,(blank.shape[1]//2,blank.shape[0]//2), (0,0,255), thickness=4)
cv.imshow('Line', blank)

#write text
cv.putText(blank, "Kite", (150, 290),cv.FONT_HERSHEY_SIMPLEX,1.0, (255,0,255), 2)
cv.imshow("Text in image", blank)
cv.waitKey(0)

cv.destroyAllWindows()