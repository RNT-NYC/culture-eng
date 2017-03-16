import cv2
import numpy as np

img1 = cv2.imread('images/bapecrew.jpg')
img2 = cv2.imread('images/bapetee.jpg')

add = img1 + img2
newadd = cv2.add(img1,img2)



cv2.imshow('image', newadd)
cv2.waitKey(0)
cv2.destroyAllWindows()
