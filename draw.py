import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
blank = np.zeros(img.shape, dtype='uint8') # create a blank image with the same shape as the original image, filled with zeros (black)

cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0, 255, 0 # paint the blank image green (BGR format)
cv.imshow('Green', blank) # you can also paint a specific region of the image, for example, the top left corner
blank[0:100, 0:100] = 255, 0, 0 # paint the top left corner blue
cv.imshow('Red', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=cv.FILLED) # draw a filled rectangle, you can also specify the thickness of the rectangle, for example, thickness=5 will draw a rectangle with a thickness of 5 pixels
# u can make the rectangle dimensions dynamic by using the shape of the image, for example, (0, 0) is the top left corner and (blank.shape[1]//2, blank.shape[0]//2) is the center of the image
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=cv.FILLED) # draw a filled circle, the center of the circle is at the center of the image, the radius is 40 pixels, and the color is red (BGR format)
# u can also specify the thickness of the circle, for example, thickness=5 will draw a circle with a thickness of 5 pixels or -1 will draw a filled circle
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello World', (255, 255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2) # write text on the image, the text is 'Hello World', the position of the text is (255, 255), the font is FONT_HERSHEY_SIMPLEX, the font scale is 1.0, the color is white (BGR format), and the thickness is 2 pixels
cv.imshow('Text', blank)

cv.waitKey(0) # keyboard binding function, it waits for a key to be pressed, and then it will destroy the window