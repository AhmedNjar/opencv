import cv2 as cv

img = cv.imread('photos/cat1.jpg')
print(img.shape) # (height, width, channels)
print(img.size) # total number of pixels (height * width * channels)
print(img.dtype) # data type of the image (uint8)

cv.imshow('cat1', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos, Live Video
    width  = int(frame.shape[1] * scale) # width of the frame 
    height = int(frame.shape[0] * scale) # height of the frame 
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0) # 0 is the default camera, you can also specify a video file path 'videos/dog.mp4'

def changeRes(width, height):
    # Live video
    capture.set(3, width) # 3 is the property id for width
    capture.set(4, height) # 4 is the property id for height

resized_image = rescaleFrame(img, scale=0.5)
cv.imshow('Resized Image', resized_image)
cv.waitKey(0) # keyboard binding function, it waits for a key to be pressed, and then it will destroy the window

"""
dimensions = None
    (h, w) = frame.shape[:2]

    if width is None and height is None:
        return frame
    if width is None:
        r = height / float(h)
        dimensions = (int(w * r), height)
    else:
        r = width / float(w)
        dimensions = (width, int(h * r))

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
"""