import cv2

img = cv2.imread("i.jpg")

result = cv2.Laplacian(img, cv2.CV_64F)
result = cv2.convertScaleAbs(result)

cv2.imshow("Original", img)
cv2.imshow("Laplacian", result)
cv2.waitKey(0)
cv2.destroyAllWindows()