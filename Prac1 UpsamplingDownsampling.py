import cv2

img = cv2.imread("a.jpg")

cv2.imshow("Original", img)

down = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("Downsampled", down)

up = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
cv2.imshow("Upsampled", up)

cv2.waitKey(0)
cv2.destroyAllWindows()