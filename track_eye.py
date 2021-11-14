from keras.models import model_from_json
from tkinter import * 
import threading
import pandas as pd
import numpy as np
import cv2
import os

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)
_, img = cap.read()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

def show_frame():
    global img
    while True:
        _, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x,y,w,h) in faces:
            img = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(img, 1.3, 5) # detect eyes
            width = np.size(img, 1) # get face frame width
            height = np.size(img, 0) # get face frame height
            for (x, y, w, h) in eyes:
                if y > height / 2:
                    pass
                eyecenter = x + w / 2  # get the eye center
                if eyecenter < width * 0.5:
                    img = img[y:y + h, x:x + w]
                    img = cv2.resize(img, dsize=(100, 100))
                    cv2.imshow("eye", img)
        interrupt = cv2.waitKey(10)
        if interrupt & 0xFF == 27: # esc key
            break

def tkinter_frame():
    global img
    frame = Tk()  
    frame.attributes('-fullscreen',True) 
    
    myCanvas = Canvas(frame)
    myCanvas.pack(fill=BOTH, expand=True)
    def predict_center():
        global x, y, img
        img = np.array(img).reshape(100*100*3)
        img = img.astype('float32')
        img /= 255
        prediction = loaded_model.predict(img)
        x = prediction[0]
        y = prediction[1]
        print(x, y)
        create_circle(x, y, 10, myCanvas)

    def create_circle(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        dot = canvasName.create_oval(x0, y0, x1, y1, fill="red")
        predict_center()
    
    predict_center()
    frame.mainloop()


t1 = threading.Thread(target=show_frame)
t2 = threading.Thread(target=tkinter_frame)

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join() 