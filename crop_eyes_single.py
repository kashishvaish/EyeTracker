import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

img = cv2.imread("C:/Users/hp/OneDrive/Desktop/Eye Tracker/images/train/897.17.12012021162154.jpg")
gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
for (x,y,w,h) in faces:
    roi_gray = gray_frame[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5) # detect eyes
    width = np.size(roi_gray, 1) # get face frame width
    height = np.size(roi_gray, 0) # get face frame height
    left_eye_status = False
    right_eye_status = False
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = roi_gray[y:y + h, x:x + w]
            left_eye = cv2.resize(left_eye, dsize=(100, 100))
            left_eye_status = True
            # cv2.imshow("eye", left_eye)
            cv2.imwrite('left_bw.jpg', left_eye)
        if eyecenter > width * 0.5:
            right_eye = roi_gray[y:y + h, x:x + w]
            right_eye = cv2.resize(right_eye, dsize=(100, 100))
            right_eye_status = True
            # cv2.imshow("eye", left_eye)
            cv2.imwrite('right_bw.jpg', right_eye)
    # if left_eye_status and right_eye_status:
    #     eyes = cv2.hconcat([left_eye, right_eye])
    #     cv2.imshow("eye", eyes)
    #     cv2.imwrite('.jpg', eyes)

            