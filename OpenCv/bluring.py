import cv2 as cv

img = cv.resize(cv.imread("assets/photo/img4.jpg"),(500,500), interpolation = cv.INTER_AREA)
cv.imshow("image",img)

#averaging
avgBlur = cv.blur(img, (3,3))
cv.imshow("Average blur", avgBlur)

#guassian blur : less blur than averaging but loks natural
gauss = cv.GaussianBlur(img, (3,3), 0.0)
cv.imshow("gaussian blur", gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow("median blur",median)


cv.waitKey(0)
cv.destroyAllWindows()