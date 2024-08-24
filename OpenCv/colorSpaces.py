import cv2 as cv
import matplotlib.pyplot as plt

img = cv.resize(cv.imread("assets/photo/img7.jpg"), (500,500), interpolation=cv.INTER_AREA)
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

#bgr to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("lab", lab)

# print invert colour because pyplot reads color in RGB format while opencv reads in BGR format
plt.imshow(img)
plt.show()

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

plt.imshow(rgb)
plt.show()

# we also can convrt colour from HSV to BGR

cv.destroyAllWindows()