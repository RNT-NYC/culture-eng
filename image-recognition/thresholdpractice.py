import cv2
import numpy as np

img = cv2.imread('images/bapehard.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

img2 = cv2.imread('images/bapeeasy.jpg')
retval3, threshold3 = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)

grayscaled2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
retval4, threshold4 = cv2.threshold(grayscaled2, 40, 255, cv2.THRESH_BINARY)



cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('threshold3', threshold3)
cv2.imshow('threshold4', threshold4)
cv2.waitKey(0)
cv2.destroyAllWindows()


