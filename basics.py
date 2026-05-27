import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert the image to grayscale
cv.imshow('Gray', gray)

# Blur the image
# there are different types of blurring techniques, such as average blur, Gaussian blur, median blur, etc. In this example, we will use Gaussian blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) # blur the image using a Gaussian blur, the kernel size is (7, 7), and the border type is BORDER_DEFAULT
# kernel size must be positive and odd, for example, (1, 1), (3, 3), (5, 5), etc. The larger the kernel size, the more blurred the image will be
cv.imshow('Blur', blur)

# Edge Cascade
# there are different types of edge detection algorithms, such as Canny edge detection, Sobel edge detection, etc. In this example, we will use Canny edge detection
canny = cv.Canny(img, 125, 175) # detect edges in the image using the Canny edge detection algorithm, the first parameter is the input image, the second parameter is the lower threshold for the hysteresis procedure, and the third parameter is the upper threshold for the hysteresis procedure
# we can reduce the thresholds to get more edges, for example, canny = cv.Canny(img, 50, 150) will give us more edges, while canny = cv.Canny(img, 200, 250) will give us fewer edges
# we also can reduce the edges by blurring the image before applying the Canny edge detection algorithm, for example, canny = cv.Canny(blur, 125, 175) will give us fewer edges than canny = cv.Canny(img, 125, 175) because the blur will reduce the noise in the image and make it easier for the Canny edge detection algorithm to detect the edges
cv.imshow('Canny Edges', canny)

# Dilating the image
# dilating the image will increase the white region in the image or the size of the foreground object. It is useful for increasing the size of the edges detected by the Canny edge detection algorithm
dilated = cv.dilate(canny, (7, 7), iterations=3) # dilate the image using a kernel of size (7, 7) and the number of iterations is 3, which means that the dilation will be applied 3 times
cv.imshow('Dilated', dilated)

# Eroding the image
# eroding the image will decrease the white region in the image or the size of the foreground object. It is useful for decreasing the size of the edges detected by the Canny edge detection algorithm
eroded = cv.erode(dilated, (7, 7), iterations=3) # erode the image using a kernel of size (7, 7) and the number of iterations is 3, which means that the erosion will be applied 3 times
cv.imshow('Eroded', eroded)

# Resize the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # resize the image to a specific size, the first parameter is the input image, the second parameter is the desired size of the output image, and the third parameter is the interpolation method, which is used to determine how the pixel values are calculated when resizing the image. In this example, we
# will use the INTER_CUBIC interpolation method, which is a good choice for resizing images because it produces a smoother result than the INTER_NEAREST interpolation method, which is the default interpolation method. The INTER_CUBIC interpolation method uses a cubic convolution algorithm to calculate the pixel values when resizing the image, which results in a smoother image than the INTER_NEAREST interpolation method, which simply takes the nearest pixel value when resizing the image.
cv.imshow('Resized', resized)

# Cropping the image
cropped = img[50:200, 200:400] # crop the image by specifying the region of interest (ROI) using slicing, the first parameter is the starting row index, the second parameter is the ending row index, the third parameter is the starting column index, and the
# fourth parameter is the ending column index. In this example, we will crop the image from row index 50 to 200 and column index 200 to 400, which will give us a cropped image of size (150, 200)
cv.imshow('Cropped', cropped)

cv.waitKey(0) # keyboard binding function, it waits for a key to be pressed, and then it will destroy the window