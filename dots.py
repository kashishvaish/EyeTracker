from tkinter import * 
import random
import cv2
import os
import threading
import datetime

if not os.path.exists("images"):
    os.makedirs("images")
if not os.path.exists("images/train"):
    os.makedirs("images/train")
if not os.path.exists("images/test"):
    os.makedirs("images/test")


mode = 'train'
directory = 'images/'+mode+'/'
  


cap = cv2.VideoCapture(0)
_, img = cap.read()

def show_frame():
    global img
    while True:
        _, img = cap.read()
        cv2.imshow("test", img)
        interrupt = cv2.waitKey(10)
        if interrupt & 0xFF == 27: # esc key
            break

def tkinter_frame():
    frame = Tk()  
    frame.attributes('-fullscreen',True) 
    
    myCanvas = Canvas(frame)
    myCanvas.pack(fill=BOTH, expand=True)
    def random_circle():
        global x, y
        x = random.randint(0, 1355)
        y = random.randint(0, 756)
        print(x, y)
        create_circle(x, y, 20, myCanvas)

    def create_circle(x, y, r, canvasName): #center coordinates, radius
        def on_click():
            canvasName.delete(dot)
            random_circle()
            cv2.imwrite(directory+ str(x) + '.' + str(y) + '.' + datetime.datetime.now().strftime("%m%d%Y%H%M%S") +'.jpg', img)

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        dot = canvasName.create_oval(x0, y0, x1, y1, fill="red")
        canvasName.tag_bind(dot, '<Button-1>', lambda e: on_click())
    
    random_circle()
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