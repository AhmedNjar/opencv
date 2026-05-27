import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # create a translation matrix, the first row is [1, 0, x] and the second row is [0, 1, y], where x is the translation in the x-axis and y is the translation in the y-axis
    # why [1, 0, x] and [0, 1, y]? because the translation matrix is a 2x3 matrix that is used to perform the translation operation on the image. The first row of the translation matrix is [1, 0, x], which means that the x-coordinate of the output image will be equal to the x-coordinate of the input image plus x. The second row of the translation matrix is [0, 1, y], which means that the y-coordinate of the output image will be equal to the y-coordinate of the input image plus y. The first two columns of the translation matrix are used to perform the scaling and rotation operations on the image, but since we are only performing translation, we set them to 1 and 0 respectively. The last column of the translation matrix is used to perform the translation operation on the image, where x is the translation in the x-axis and y is the translation in the y-axis. For example, if we want to translate the image 100 pixels to the right and 50 pixels down, we can set x to 100 and y to 50, which will give us the translation matrix [[1, 0, 100], [0, 1, 50]].
    dimensions = (img.shape[1], img.shape[0]) # get the dimensions of the image, the width is img.shape[1] and the height is img.shape[0]
    return cv.warpAffine(img, transMat, dimensions) # apply the translation to the image using the warpAffine function, the first parameter is the input image, the second parameter is the translation matrix, and the third parameter is the dimensions of the output image

# -x will translate the image to the left, -y will translate the image up, x will translate the image to the right, and y will translate the image down. For example, if we want to translate the image 100 pixels to the left and 50 pixels up, we can set x to -100 and y to -50, which will give us the translation matrix [[1, 0, -100], [0, 1, -50]].
translated = translate(img, 100, 100) # translate the image 100 pixels to the right and 100 pixels down
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None): # rotPoint is the point around which we want to rotate the image, if it is None, we will rotate the image around the center of the image
    (height, width) = img.shape[:2] # get the height and width of the image, :2 means that we are only interested in the first two values of the shape, which are the height and width of the image, and we ignore the third value, which is the number of channels in the image
    # channel means the number of color channels in the image, for example, a color image has 3 channels (BGR), while a grayscale image has only 1 channel (gray)
    if rotPoint is None: # if the rotation point is not specified, we will rotate the image around the center of the image
        rotPoint = (width // 2, height // 2) # set the rotation point to the center of the image
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # create a rotation matrix using the getRotationMatrix2D function, the first parameter is the rotation point, the second parameter is the angle of rotation in degrees, and the third parameter is the scale factor, which is set to 1.0 in this case
    dimensions = (width, height) # set the dimensions of the output image to be the same as the input image
    return cv.warpAffine(img, rotMat, dimensions) # apply the rotation to the image using the warpAffine function, the first parameter is the input image, the second parameter is the rotation matrix, and the third parameter is the dimensions of the output image 

rotated = rotate(img, 45) # rotate the image 45 degrees around the center of the image
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # resize the image to a specific size, the first parameter is the input image, the second parameter is the desired size of the output image, and the third parameter is the interpolation method, which
# is used to determine how the pixel values are calculated when resizing the image. In this example, we will use the INTER_CUBIC interpolation method, which is a good choice for resizing images because it produces a smoother result than the INTER_NEAREST interpolation method, which is the default interpolation method. The INTER_CUBIC interpolation method uses a cubic convolution algorithm to calculate the pixel values when resizing the image, which results in a smoother image than the INTER_NEAREST interpolation method, which simply takes the nearest pixel value when resizing the image.
cv.imshow('Resized', resized)

# Flipping
flipped = cv.flip(img, 0) # flip the image vertically, the second parameter is the flip code, which determines how the image will be flipped. If the flip code is 0, the image will be flipped vertically. If the flip code is 1, the image will be flipped horizontally. If the flip code is -1, the image will be flipped both vertically and horizontally. In this example, we will flip the image vertically by setting the flip code to 0.
cv.imshow('Flipped', flipped)

# Cropping
cropped = img[50:200, 200:400] # crop the image by specifying the region of interest (ROI) using slicing, the first parameter is the starting row index, the second parameter is the ending row index, the third parameter is the starting column index, and the fourth parameter is the ending column index. In this example, we will crop the image from row index 50 to 200 and column index 200 to 400, which will give us a cropped image of size (150, 200)
cv.imshow('Cropped', cropped)

cv.waitKey(0) # keyboard binding function, it waits for a key to be pressed, and then it will destroy the window