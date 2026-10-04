import cv2

img = cv2.imread("a.jpg")

x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
result = cv2.convertScaleAbs(x + y)

cv2.imshow("Original", img)
cv2.imshow("Gradient", result)
cv2.waitKey(0)
cv2.destroyAllWindows()