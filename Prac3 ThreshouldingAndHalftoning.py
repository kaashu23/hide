import cv2

img = cv2.imread("a.jpg",0)
_, result = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Threshold", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
