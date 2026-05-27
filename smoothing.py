import cv2 as cv
import numpy as np

img = cv.imread('photos/cat2.jpg')
cv.imshow('Cat', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)
# what happened is that the kernel (3,3) is moving across the image and taking the average of the pixel values in that kernel and replacing the center pixel with that average value. This results in a blurred image.

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)
# The Gaussian Blur is similar to the average blur but it uses a weighted average where the weights are determined by a Gaussian function. This means that the pixels closer to the center of the kernel have more influence on the final value than the pixels farther away. This results in a smoother blur compared to the average blur.
# 0 is the standard deviation in the X direction. If it is set to 0, it is calculated from the kernel size.

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
# The Median Blur is a non-linear filter that replaces the center pixel with the median of the pixel values in the kernel. This is particularly effective for removing salt-and-pepper noise from an image. The kernel size must be an odd integer greater than 1.      

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 9, 75, 75) # The first parameter is the diameter of the pixel neighborhood, the second parameter is the sigma in the color space, and the third parameter is the sigma in the coordinate space. This filter is particularly effective for reducing noise while keeping edges sharp.
cv.imshow('Bilateral Blur', bilateral)
# The Bilateral Blur is a non-linear filter that preserves edges while blurring the image. It does this by considering both the spatial distance and the intensity difference between pixels. The first parameter is the diameter of the pixel neighborhood, the second parameter is the sigma in the color space, and the third parameter is the sigma in the coordinate space. This filter is particularly effective for reducing noise while keeping edges sharp.    
# In summary, the choice of blur method depends on the specific requirements of the application. The average blur is simple and fast but can produce a very blurry image. The Gaussian blur provides a smoother result but can still blur edges. The median blur is effective for removing noise while preserving edges, and the bilateral blur is excellent for reducing noise while keeping edges sharp.  

cv.waitKey(0)