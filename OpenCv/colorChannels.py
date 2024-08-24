import cv2 as cv
import numpy as np

img = cv.resize(cv.imread("assets/photo/img7.jpg"), (500,500), interpolation=cv.INTER_AREA)
cv.imshow("image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b,g,r = cv.split(img)
cv.imshow("blue", b)
cv.imshow("green",g)
cv.imshow("red",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("merged", merged)

blue = cv.merge([b, blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue channel", blue)
cv.imshow("green channel", green)
cv.imshow("red channel", red)

print(blue.shape)
cv.waitKey(0)
cv.destroyAllWindows()