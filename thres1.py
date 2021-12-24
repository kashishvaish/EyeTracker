# Python program to illustrate
# simple thresholding type on an image
     
# organizing imports
import cv2
import numpy as np
 
# path to input image is specified and 
# image is loaded with imread command
image1 = cv2.imread('C:/Users/hp/OneDrive/Desktop/Eye Tracker/left_eyes_data/0.0.12032021133553.jpg.jpg',0)

 
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
 
# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow('1.jpg', thresh1)
cv2.imshow('2.jpg', thresh2)
cv2.imshow('3.jpg', thresh3)
cv2.imshow('4.jpg', thresh4)
cv2.imshow('5.jpg', thresh5)
   
# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()