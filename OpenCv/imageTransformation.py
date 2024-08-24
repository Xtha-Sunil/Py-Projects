import cv2 as cv 
import numpy as np 

img = cv.imread("assets/photo/img3.webp")
cv.imshow("image", img)


#translation
#warAffine funcyion is used to translate te image for this we neeed to build affine tranlation mtrix of 2*3 i.e [[scale, shear, Tx], [shear, scale, Ty]]
#float32 function is used increase the precision of transMatrix
def translate(img, x,y):
    transMat= np.float32([[1,0,x], [0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

translated = translate(img,-30,50)
cv.imshow("translated", translated)


#rotate the image 
def rotate(img, angle, rotPoint=None):
    (height, width )= img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    dimension = (width,height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img,90)
cv.imshow("rotated", rotated)

#resize
resized = cv.resize(img, (300,300), interpolation=cv.INTER_AREA)

#flipping the imzge
flip = cv.flip(img, -1)
cv.imshow("flip", flip)

#doesnt matter 0-1 or 1-0 / same as -1
a = cv.flip(img, 0)
b = cv.flip(a, 1)
cv.imshow("flip 0-1", b)

aa = cv.flip(img, 0)
bb = cv.flip(aa, 1)
cv.imshow("flip 1-0", bb)
'''
0 = x-axis or vertically
1 = y-axis or horizontally
-1 = both horizontally and vertically
'''

#cropping the image
# syntax [start_row:end_row, start_column:end_column] 
crop = img[0:200, 0:200]
cv.imshow("cropped", crop)

cv.waitKey(0)


'''
INTER_NEAREST: Nearest-neighbor interpolation. This method selects the nearest pixel value to the new pixel location. It's the fastest but can result in blocky or pixelated images.

INTER_LINEAR: Bilinear interpolation. This method takes a weighted average of the four nearest pixels to the new pixel location. It produces smoother results compared to nearest-neighbor interpolation but may still introduce some blurring.

INTER_CUBIC: Bicubic interpolation. This method takes a weighted average of the sixteen nearest pixels to the new pixel location, using a cubic polynomial. It produces smoother results than bilinear interpolation but requires more computational resources.

INTER_AREA: Area-based resampling. This method resamples the image using pixel area relation. It's typically used for downsampling (reducing the size of the image) as it preserves the area of each pixel, which can help maintain sharpness and reduce aliasing artifacts.
'''