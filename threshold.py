import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2

source = "left_eyes_data"
destination = "threshold_data/"

if not os.path.exists("threshold_data"):
    os.makedirs("threshold_data")

for filename in os.listdir(source)[:1]:
    img = cv.imread(os.path.join(source,filename))
    cv.imshow('Original', img)
    cv.waitKey(0)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
# Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
    cv2.imshow('Sobel X', sobelx)
    cv2.waitKey(0)
    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)
    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    cv2.waitKey(0)
# Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=20, threshold2=50) # Canny Edge Detection
# Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # ret, th1 = cv.threshold(img, 90, 255, cv.THRESH_TOZERO)
    # cv.imwrite(destination + filename + '.jpg', th1)
    