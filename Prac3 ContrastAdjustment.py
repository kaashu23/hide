import cv2
import numpy as np

img = cv2.imread("a.jpg")
gamma = 4
result = np.uint8(255 * (img / 255) ** gamma)

cv2.imshow("Original", img)
cv2.imshow("Gamma", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
