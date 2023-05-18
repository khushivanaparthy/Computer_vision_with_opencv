#1
import cv2

img = cv2.imread("C:\\Users\\ghant\\OneDrive\\Desktop\\me.jpg")

blur_img = cv2.GaussianBlur(img,(5,5),0)     

cv2.imwrite('blur_image.jpg',blur_img)