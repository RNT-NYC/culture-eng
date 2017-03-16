import numpy as np
import cv2


img = cv2.imread('images/bape.jpg', cv2.IMREAD_COLOR)

bapeshirt = img[300:650, 134:371]
img[0:350,0:237] = bapeshirt



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
