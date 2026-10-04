import cv2

img = cv2.imread("a.jpg")
temp = cv2.imread("a.jpg")

result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
_, _, _, loc = cv2.minMaxLoc(result)

h, w = temp.shape[:2]
cv2.rectangle(img, loc, (loc[0]+w, loc[1]+h), (0,0,255), 2)

cv2.imshow("Original Image", cv2.imread("a.jpg"))
cv2.imshow("Matched Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
