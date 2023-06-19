import cv2

# Load the images
img1 = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\space.jpg')
img2 = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\dora.jpg')

# Get the dimensions of the images
rows, cols, channels = img2.shape

# Copy a portion of img2 and paste it onto img1 at (x, y) = (50, 50)
roi = img1[50:50+rows, 50:50+cols]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg, img2_fg)
img1[50:50+rows, 50:50+cols] = dst

# Show the result
cv2.imshow('result', img1)
cv2.waitKey(0)