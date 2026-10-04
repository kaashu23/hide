import cv2
import numpy as np

img = cv2.imread("a.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge-based segmentation
edges = cv2.Canny(gray, 50, 150)

# Circle detection
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 150,
                           param1=50, param2=30, minRadius=10, maxRadius=50)

if circles is not None:
    for x, y, r in np.uint16(np.around(circles[0])):
        cv2.circle(img, (x, y), r, (0, 0, 255), 2)

# Region-based segmentation
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
num, labels = cv2.connectedComponents(binary)[:2]

regions = np.zeros_like(img)
for i in range(1, num):
    regions[labels == i] = 255

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("Circles", img)
cv2.imshow("Regions", regions)

cv2.waitKey(0)
cv2.destroyAllWindows()
