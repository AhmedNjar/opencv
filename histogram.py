import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)
cv.imshow('Mask', circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask Applied to Grayscale', mask)

# Grayscale histogram
# gray_hist = cv.calcHist([img], [0], mask, [256], [0,256]) # The cv.calcHist function is used to calculate the histogram of the grayscale image. The parameters are as follows:
# [gray]: The source image for which the histogram is to be calculated. It should be a single-channel image (grayscale).
# [0]: The index of the channel for which the histogram is to be calculated. Since the image is grayscale, there is only one channel (index 0).
# None: A mask image. If you want to calculate the histogram for the entire image, you can set this to None. If you want to calculate the histogram for a specific region of the image, you can provide a binary mask where the pixels of interest are set to 255 and the rest are set to 0.
# [256]: The number of bins for the histogram. In this case, we are using 256 bins to cover the range of pixel intensity values from 0 to 255.
# [0,256]: The range of pixel intensity values to be considered for the histogram. The lower boundary is 0 and the upper boundary is 256 (exclusive), which means that the histogram will include pixel intensity values from 0 to 255. 
# print(gray_hist)
# plt.figure()
# plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of Pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
    
#plt.show()

# Color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256]) # The cv.calcHist function is used to calculate the histogram for each color channel (blue, green, red) of the original image. The parameters are as follows:
    # [img]: The source image for which the histogram is to be calculated. It should be a multi-channel image (color).
    # [i]: The index of the channel for which the histogram is to be calculated. Since the image is in BGR format, the indices are 0 for blue, 1 for green, and 2 for red.
    # None: A mask image. If you want to calculate the histogram for the entire image, you can set this to None. If you want to calculate the histogram for a specific region of the image, you can provide a binary mask where the pixels of interest are set to 255 and the rest are set to 0.
    # [256]: The number of bins for the histogram. In this case, we are using 256 bins to cover the range of pixel intensity values from 0 to 255.
    # [0,256]: The range of pixel intensity values to be considered for the histogram. The lower boundary is 0 and the upper boundary is 256 (exclusive), which means that the histogram will include pixel intensity values from 0 to 255.
    print(hist)
    plt.plot(hist, color=color)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)