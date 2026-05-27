import cv2 as cv

# Read an image
#img = cv.imread('photos/cat1.jpg')
#cv.imshow('cat1', img)
#cv.waitKey(0) # keyboard binding function, it waits for a key to be pressed, and then it will destroy the window
# cv.destroyAllWindows()

# Read a video
capture = cv.VideoCapture(0) # 0 is the default camera, you can also specify a video file path 'videos/dog.mp4'

while True:
    isTrue, frame = capture.read() # read the video frame by frame, isTrue is a boolean that indicates if the frame was read successfully, frame is the actual frame

    cv.imshow('Video', frame) # display the video

    if cv.waitKey(20) & 0xFF == ord('d'): # if 'd' is pressed, break the loop
        break

capture.release() # release the video capture object, it is important to release the video capture object after you are done with it, otherwise it will keep the camera on and consume resources
cv.destroyAllWindows() # destroy all the windows, it is important to destroy all the windows after you are done with them, otherwise they will keep consuming resources