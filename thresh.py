import cv2 as cv
import numpy as np

img = cv.imread('photos/cat2.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
_, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # The cv.threshold function is used to apply a simple thresholding operation to the grayscale image. The parameters are as follows:
# [gray]: The source image for which the thresholding operation is to be applied. It should be a single-channel image (grayscale).
# 125: The threshold value. This is the value that is used to classify the pixel values. If a pixel value is greater than the threshold value, it is set to the maximum value (255 in this case). If a pixel value is less than or equal to the threshold value, it is set to 0.
# 255: The maximum value to use with the THRESH_BINARY thresholding type. This is the value that is assigned to the pixels that are greater than the threshold value.
# cv.THRESH_BINARY: The type of thresholding to be applied. In this case, we are using the THRESH_BINARY type, which means that the pixel values will be set to either 0 or the maximum value (255) based on the thresholding condition.    
cv.imshow('Simple Threshold', thresh)

# inverse thresholding
_, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV) # The cv.threshold function is used to apply an inverse thresholding operation to the grayscale image. The parameters are the same as in the previous example, but the thresholding type is different:
# [gray]: The source image for which the thresholding operation is to be applied. It should be a single-channel image (grayscale).
# 125: The threshold value. This is the value that is used to classify the pixel values. If a pixel value is greater than the threshold value, it is set to 0. If a pixel value is less than or equal to the threshold value, it is set to the maximum value (255 in this case).
# 255: The maximum value to use with the THRESH_BINARY_INV thresholding type. This is the value that is assigned to the pixels that are less than or equal to the threshold value.
# cv.THRESH_BINARY_INV: The type of thresholding to be applied. In this case, we are using the THRESH_BINARY_INV type, which means that the pixel values will be set to either 0 or the maximum value (255) based on the inverse of the thresholding condition.    
cv.imshow('Inverse Threshold', thresh_inv)

# Adaptive thresholding
thresh_adapt = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) # The cv.adaptiveThreshold function is used to apply an adaptive thresholding operation to the grayscale image. The parameters are as follows:
# [gray]: The source image for which the adaptive thresholding operation is to be applied. It should be a single-channel image (grayscale).
# 255: The maximum value to use with the adaptive thresholding. This is the value that is assigned to the pixels that are classified as foreground (greater than the adaptive threshold value).
# cv.ADAPTIVE_THRESH_MEAN_C: The adaptive method to be used. In this case, we are using the ADAPTIVE_THRESH_MEAN_C method, which calculates the adaptive threshold value as the mean of the neighborhood area minus a constant (C).
# cv.THRESH_BINARY: The type of thresholding to be applied. In this case, we are using the THRESH_BINARY type, which means that the pixel values will be set to either 0 or the maximum value (255) based on the adaptive thresholding condition.
# 11: The block size to be used for the adaptive thresholding. This is the size of the neighborhood area that is used to calculate the adaptive threshold value for each pixel. It should be an odd number (e.g., 3, 5, 7, etc.).
# 3: The constant (C) to be subtracted from the mean or weighted mean calculated for the adaptive thresholding. This constant is used to fine-tune the thresholding result. A positive value will decrease the threshold value, while a negative value will increase it. In this case, we are using a constant of 3, which means that the adaptive threshold value will be the mean of the neighborhood area minus 3.    
cv.imshow('Adaptive Threshold', thresh_adapt)
# You can inverse the adaptive thresholding result by using cv.THRESH_BINARY_INV instead of cv.THRESH_BINARY in the cv.adaptiveThreshold function.

# Otsu's thresholding
_, thresh_otsu = cv.threshold(gray, 125, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) # The cv.threshold function is used to apply Otsu's thresholding operation to the grayscale image. The parameters are as follows:
# [gray]: The source image for which the thresholding operation is to be applied. It should be a single-channel image (grayscale).
# 125: The threshold value. This value is ignored when using Ots u's thresholding, as the optimal threshold value is automatically determined by the algorithm.
# 255: The maximum value to use with the Otsu's thresholding. This is the value that is assigned to the pixels that are classified as foreground (greater than the optimal threshold value).
# cv.THRESH_BINARY + cv.THRESH_OTSU: The type of thresholding to be applied. In this case, we are using a combination of the THRESH_BINARY type and the THRESH_OTSU flag. The THRESH_OTSU flag tells the function to automatically determine the optimal threshold value using Otsu's method, which minimizes the intra-class variance of the pixel values.    
cv.imshow('Otsu Threshold', thresh_otsu)    

cv.waitKey(0)