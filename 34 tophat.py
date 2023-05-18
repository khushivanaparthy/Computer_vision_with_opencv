# 34
import cv2
# Getting the kernel to be used in Top-Hat
filterSize =(3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,filterSize)
# Reading the image named 'input.jpg'
input_image = cv2.imread("C:\\Users\\ghant\\OneDrive\\Desktop\\shin.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
# Applying the Top-Hat operation
tophat_img = cv2.morphologyEx(input_image,cv2.MORPH_TOPHAT,kernel)
cv2.imwrite("original.png", input_image)
cv2.imwrite("tophat.png", tophat_img)
