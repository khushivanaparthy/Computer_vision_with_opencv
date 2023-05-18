#11
import cv2
import numpy as np 

img = cv2.imread("C:\\Users\\ghant\\OneDrive\\Desktop\\tpt.jpg")

rows, cols = img.shape[:2]
M = np.float32([[1 ,0 ,200],[0, 1, 100]])

affine_img = cv2.warpAffine(img, M, ( cols, rows))

cv2.imwrite('Affine_image.jpg',affine_img)