import cv2

img = cv2.imread("a.jpg", 0)
result = cv2.equalizeHist(img)

cv2.imshow("Original", img)
cv2.imshow("Equalized", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
