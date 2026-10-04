import cv2

img = cv2.imread("a.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face = cv2.CascadeClassifier(cascade_path)


faces = face.detectMultiScale(gray, 1.1, 5)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
