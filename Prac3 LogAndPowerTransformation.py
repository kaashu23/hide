import cv2
import numpy as np

img = cv2.imread("a.jpg")
log = 255 * np.log1p(img) / np.log1p(img.max())

cv2.imshow("Original", img)
cv2.imshow("Log", np.uint8(log))
cv2.waitKey(0)
cv2.destroyAllWindows()