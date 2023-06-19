import cv2

# Load the image
img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\shinchan.jpg')

# Crop the image from (x, y) = (10, 10) to (x, y) = (300, 300)
crop_img = img[10:300, 10:300]

# Show the cropped image
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)