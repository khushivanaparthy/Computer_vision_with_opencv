import numpy as np 
import cv2
points3d = np.array([[0, 0, 0, 1],
                    [1, 0, 0 ,1],
                    [0, 1, 0, 1],
                    [0, 0, 1, 1]], dtype=np.float32)

points2d = np.array([[100, 100],
                     [200, 100],
                     [100, 200],
                     [150, 150]],dtype=np.float32)

_,camera_matrix = cv2.solve( points3d, points2d, flags=cv2.DECOMP_SVD)

print("camera matrix : \n",camera_matrix)