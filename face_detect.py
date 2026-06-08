import cv2 as cv

# face detection is different from face recognition. Face detection is the process of identifying and locating faces in an image or video, while face recognition is the process of identifying or verifying a person's identity based on their facial features.
# Haar cascades are a machine learning-based approach for object detection, including face detection. They are based on the concept of Haar-like features, which are simple rectangular features that can be used to represent the presence or absence of certain patterns in an image. The Haar cascade classifier is trained on a large dataset of positive and negative examples to learn how to detect specific objects, such as faces.
# The Haar cascade classifier works by scanning the input image at multiple scales and locations, applying the learned Haar-like features to determine if a face is present in each region. If the features match the trained model, the classifier will output a positive detection, indicating the presence of a face. The Haar cascade method is efficient and can be used in real-time applications, making it a popular choice for face detection tasks.

img = cv.imread('photos/arg1.jpg')
cv.imshow('Arg1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml') # The cv.CascadeClassifier function is used to load a pre-trained Haar cascade classifier from an XML file. The parameter 'haar_face.xml' is the filename of the XML file that contains the trained model for face detection. This file should be located in the same directory as the script or provide the correct path to the file. The Haar cascade classifier will be used to detect faces in the input image based on the features it has learned during training.

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

for (x,y,w,h) in faces_rect: # The for loop iterates over the list of detected faces, where each face is represented as a rectangle defined by its top-left corner (x, y) and its width (w) and height (h). The loop extracts these values for each detected face and uses them to draw a rectangle around the face in the original image. The cv.rectangle function is used to draw the rectangle, with the parameters specifying the image to draw on, the top-left corner of the rectangle, the bottom-right corner of the rectangle (calculated using x+w and y+h), the color of the rectangle (in this case, green), and the thickness of the rectangle's border.
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

print(f'Number of faces found = {len(faces_rect)}')

cv.imshow('Detected Faces', img)

cv.waitKey(0)