import cv2
import numpy as np

img = cv2.imread("a.jpg", 0)
temp = np.ones((3,3)) / 9
smooth = cv2.GaussianBlur(img, (5,5), 0)
sharp = cv2.filter2D(img, -1, temp)
unsharp = cv2.addWeighted(img, 1.5, smooth, -0.5, 0)

cv2.imshow("Original", img)
cv2.imshow("Smooth", smooth)
cv2.imshow("Sharp", sharp)
cv2.imshow("Unsharp", unsharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
