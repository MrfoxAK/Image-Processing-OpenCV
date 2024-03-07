import cv2
import numpy as np

# img = cv2.imread("newyork.jpg",1)
img = cv2.imread("newyork.jpg",0)

kernal = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernal, iterations=5)
img_dilation = cv2.dilate(img, kernal, iterations=5)

cv2.imshow('Original Image',img)
cv2.imshow('Erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)

if cv2.waitKey(0) & 0xFF == ord('w'):
     cv2.destroyAllWindows()




