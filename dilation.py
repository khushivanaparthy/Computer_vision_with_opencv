#4
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\ghant\\OneDrive\\Desktop\\tpt.jpg")

kernel = np.ones((5,5), np.uint8)

dilation_img = cv2. dilate(img, kernel, iterations=1)     

cv2.imwrite('dilation_image.jpg',dilation_img)