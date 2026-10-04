import cv2
import numpy as np

img = cv2.imread("a.jpg")
# img = cv2.bitwise_not(img)

# k = np.ones((5,5), np.uint8)
k = np.ones((5,5))

erosion = cv2.erode(img, k)
dilation = cv2.dilate(img, k)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)

cv2.imshow("Original", img)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
