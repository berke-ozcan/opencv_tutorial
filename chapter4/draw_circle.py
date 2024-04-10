import cv2

image = cv2.imread("../data/test1.jpg")

image = cv2.circle(image, (200,200), 150, (130, 240, 0), 20, cv2.LINE_8, None)

cv2.imshow("lol", image)
cv2.waitKey(0)
cv2.destroyAllWindows()