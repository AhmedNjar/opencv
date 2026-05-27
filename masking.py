import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 150, 255, -1) # The mask is created by drawing a filled circle on a blank image. The center of the circle is set to the center of the original image (img.shape[1]//2, img.shape[0]//2), and the radius is set to 150 pixels. The color of the circle is set to 255 (white) and the thickness is set to -1, which means that the circle will be filled. This mask will be used to isolate the area of interest in the original image.
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask) # The bitwise AND operation is applied to the original image (img) using itself as both input images and the created mask. This operation will keep the pixel values of the original image where the mask is white (255) and set the pixel values to black (0) where the mask is black (0). As a result, the output image (masked) will show only the area of the original image that corresponds to the white area of the mask, effectively isolating that part of the image.
cv.imshow('Masked', masked)

cv.waitKey(0)