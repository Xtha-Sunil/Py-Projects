'''Edges: Edges in an image represent areas where the intensity of the image changes abruptly. These changes can indicate the boundaries of objects or significant features in the image. Edge detection algorithms are used to identify these areas of rapid intensity change, typically by looking for gradients or differences in pixel values.

Contours: Contours, on the other hand, are curves that represent the boundaries of objects in an image. Contours are a higher-level representation than edges, as they are the result of connecting the points along the boundary of an object. Contours can be used to extract and represent the shape of objects in an image, which can be useful for tasks like object detection, recognition, and segmentation.
'''

import cv2 as cv
import numpy as np

img = cv.imread("assets/photo/img7.jpg")
img = cv.resize(img, (800,600), interpolation=cv.INTER_AREA )


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)

canny = cv.Canny(gray, 125, 175)
cv.imshow("canny edges", canny)

ret, thresh = cv.threshold(gray, 140,150, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) found")

blank = np.zeros(img.shape, dtype="uint8")
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("contours", blank)

cv.waitKey(0)
cv.destroyAllWindows()