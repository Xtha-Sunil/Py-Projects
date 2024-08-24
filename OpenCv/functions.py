import cv2 as cv

def rescale(frame):
    dimension = (500,500)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = rescale(cv.imread("assets/photo/img7.jpg"))
cv.imshow("image", img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("image grayscitaled", gray)

#blur : removes some noises 
# kernal size should be odd
blur = cv.GaussianBlur(img, (1,17), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

#edge cascade
#find edge in frames
canny = cv.Canny(img, 125,175)
cv.imshow("edge detection", canny)

#dilate :
dilated = cv.dilate(canny, (3,3), iterations=4)
cv.imshow("dilate", dilated)

#eroding
eroded = cv.erode(dilated, (7,7), iterations=4)
cv.imshow("erode", eroded)

#resize
resized = cv.resize(img, (200,500), interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)

#crop
crop = img[0:200, 250:400]
cv.imshow("crop", crop)

cv.waitKey(0)
cv.destroyAllWindows()