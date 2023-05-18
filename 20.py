#20
import cv2
import numpy as np

img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\sh.jpg')
kernel = np.array([[0,1,0], [1,-4,1], [0,1,0]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()