#3
import cv2

img = cv2.imread("C:\\Users\\ghant\\OneDrive\\Desktop\\manu.jpg")

outline_img = cv2.Canny(img,100,200)     

cv2.imwrite('outline_image.jpg',outline_img)