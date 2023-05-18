#17
import cv2
import numpy as np

img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\shin.jpg',0)

# Output dtype = cv2.CV_8U
sobel_x = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

cv2.imwrite('sobel_x.jpg',sobel_x)
