import cv2
import numpy as np

img = cv2.imread("a.jpg")

kernel = np.ones((3,3)) / 9
result = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Convolved", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
