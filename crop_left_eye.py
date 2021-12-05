import numpy as np
import cv2
import os

source = "images/train"
destination = "left_eyes_data/"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

if not os.path.exists("left_eyes_data"):
    os.makedirs("left_eyes_data")

for filename in os.listdir(source):
    img = cv2.imread(os.path.join(source,filename))
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray_frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5) # detect eyes
        width = np.size(roi_gray, 1) # get face frame width
        height = np.size(roi_gray, 0) # get face frame height
        for (x, y, w, h) in eyes:
            if y > height / 2:
                pass
            eyecenter = x + w / 2  # get the eye center
            if eyecenter < width * 0.5:
                left_eye = roi_gray[y:y + h, x:x + w]
                left_eye = cv2.resize(left_eye, dsize=(100, 100))
                cv2.imshow("eye", left_eye)
                cv2.imwrite(destination + filename + '.jpg', left_eye)