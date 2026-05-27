import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/cat2.jpg')
cv.imshow('Cat', img)

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)
# you can do all of the other to BGR
# But u cant convert from gray for example for HSV directly

cv.waitKey(0)

# matplotlip "RGB"
plt.imshow(img)
plt.show()
