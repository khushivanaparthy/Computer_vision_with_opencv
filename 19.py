#19
import cv2
import numpy as np

# Load the image
img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\shin.jpg', 0)

# Apply the Sobel operator along the X axis
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply the Sobel operator along the Y axis
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine the results of the X and Y axis to get the final edge detection result
edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Display the result
cv2.imwrite('Edge_detection.jpg', edges)
