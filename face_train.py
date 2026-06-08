import os
import cv2 as cv
import numpy as np

people = ['Ben_Afflek', 'Trika', 'Messi']
DIR = r'Faces/train'

def create_train():
    features = []
    labels = []

    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            haar_cascade = cv.CascadeClassifier('haar_face.xml')

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]

            features.append(faces_roi)
            labels.append(label)

    features = np.array(features, dtype='object')
    labels = np.array(labels)

    return features, labels

features, labels = create_train()

print('Training done ------------------')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)