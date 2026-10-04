import cv2

img = cv2.imread("a.jpg")

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

cv2.imshow("Original", img)
cv2.imshow("Gaussian - Linear", gaussian)
cv2.imshow("Median - Nonlinear", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
