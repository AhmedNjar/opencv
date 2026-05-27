import cv2 as cv
import numpy as np

img = cv.imread('photos/cat2.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
laplacian = cv.Laplacian(gray, cv.CV_64F) # The cv.Laplacian function is used to apply the Laplacian operator to the grayscale image. The parameters are as follows:
# [gray]: The source image for which the Laplacian operator is to be applied. It should be a single-channel image (grayscale).
# cv.CV_64F: The desired depth of the destination image. In this case, we are using CV_64F, which means that the output image will have a depth of 64 bits (floating-point). This is necessary to capture the negative values that can result from the Laplacian operator, as it calculates the second derivative of the image. Using a floating-point depth allows us to preserve the full range of values, including negative values, which can be important for edge detection and other applications.    
laplacian = np.uint8(np.absolute(laplacian)) # The np.absolute function is used to take the absolute value of the Laplacian result, which can contain negative values due to the nature of the second derivative. The np.uint8 function is then used to convert the resulting values to an unsigned 8-bit integer format, which is suitable for displaying as an image. This step ensures that all pixel values are non-negative and within the range of 0 to 255, which is necessary for proper visualization of the edges detected by the Laplacian operator.
cv.imshow('Laplacian', laplacian)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # The cv.Sobel function is used to apply the Sobel operator to the grayscale image. The parameters are as follows:
# [gray]: The source image for which the Sobel operator is to be applied. It should be a single-channel image (grayscale).
# cv.CV_64F: The desired depth of the destination image. In this case, we are using CV_64F, which means that the output image will have a depth of 64 bits (floating-point). This is necessary to capture the negative values that can result from the Sobel operator, as it calculates the first derivative of the image. Using a floating-point depth allows us to preserve the full range of values, including negative values, which can be important for edge detection and other applications.
# 1: The order of the derivative in the x direction. In this case, we are calculating the first derivative in the x direction, which means that we are detecting edges that are vertical (i.e., changes in intensity along the horizontal axis).
# 0: The order of the derivative in the y direction. In this case, we are not calculating any derivative in the y direction, which means that we are only interested in detecting edges in the x direction. If we wanted to detect edges in the y direction, we would set this parameter to 1 and the previous parameter to 0.    
sobelx = np.uint8(np.absolute(sobelx)) # The np.absolute function is used to take the absolute value of the Sobel result, which can contain negative values due to the nature of the first derivative. The np.uint8 function is then used to convert the resulting values to an unsigned 8-bit integer format, which is suitable for displaying as an image. This step ensures that all pixel values are non-negative and within the range of 0 to 255, which is necessary for proper visualization of the edges detected by the Sobel operator in the x direction.

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobely = np.uint8(np.absolute(sobely)) 

combined_sobel = cv.bitwise_or(sobelx, sobely) # The cv.bitwise_or function is used to combine the results of the Sobel operator in the x and y directions. The parameters are as follows:
# [sobelx]: The first source image, which contains the edges detected in the x direction.
# [sobely]: The second source image, which contains the edges detected in the y direction.
# None: The destination image. If you want to store the result in a new image

cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175) # The cv.Canny function is used to apply the Canny edge detection algorithm to the grayscale image. The parameters are as follows:
# [gray]: The source image for which the Canny edge detection is to be applied. It should be a single-channel image (grayscale).
# 150: The lower threshold for the hysteresis procedure. This is the minimum intensity gradient that is considered an edge. If a pixel's intensity gradient is below this threshold, it will be discarded as a non-edge.
# 175: The upper threshold for the hysteresis procedure. This is the maximum intensity gradient that is considered an edge. If a pixel's intensity gradient is above this threshold, it will be accepted as a strong edge. If a pixel's intensity gradient is between the lower and upper thresholds, it will be accepted as a weak edge only if it is connected to a strong edge.
cv.imshow('Canny', canny)

cv.waitKey(0)