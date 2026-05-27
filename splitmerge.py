import cv2 as cv
import numpy as np


img = cv.imread('photos/cat2.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue blank', blue)
cv.imshow('Green blank', green)
cv.imshow('Red blank', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)