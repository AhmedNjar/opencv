import cv2 as cv
import numpy as np

blank = np.zeros((300,300), dtype='uint8')
cv.imshow('Blank', blank)

rectangle = cv.rectangle(blank.copy(), (30,30), (270,270), 255, -1)
cv.imshow('Rectangle', rectangle)
circle = cv.circle(blank.copy(), (150,150), 150, 255, -1)
cv.imshow('Circle', circle)

# Bitwise AND --> intersection of the two shapes
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)
# The bitwise AND operation takes two binary images and performs a logical AND operation on each corresponding pixel. The result is a new image where a pixel is set to 255 (white) only if both corresponding pixels in the input images are 255 (white). In this case, the resulting image will show the area where the rectangle and circle overlap. 

# Bitwise OR --> union of the two shapes
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)
# The bitwise OR operation takes two binary images and performs a logical OR operation on each corresponding pixel. The result is a new image where a pixel is set to 255 (white) if at least one of the corresponding pixels in the input images is 255 (white). In this case, the resulting image will show the area covered by either the rectangle or the circle, including the overlapping area.   

# Bitwise XOR --> exclusive OR, only the non-overlapping areas of the two shapes
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)
# The bitwise XOR operation takes two binary images and performs a logical XOR operation on each corresponding pixel. The result is a new image where a pixel is set to 255 (white) only if the corresponding pixels in the input images are different (i.e., one is 255 and the other is 0). In this case, the resulting image will show the areas covered by either the rectangle or the circle, but not the overlapping area.    

# Bitwise NOT --> inverse of the shape
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)
# The bitwise NOT operation takes a binary image and inverts the pixel values. The result is a new image where all pixels that were 255 (white) in the input image become 0 (black), and all pixels that were 0 (black) become 255 (white). In this case, the resulting image will show the inverse of the rectangle, meaning that the area where the rectangle was will now be black, and the area outside the rectangle will be white.    


cv.waitKey(0)