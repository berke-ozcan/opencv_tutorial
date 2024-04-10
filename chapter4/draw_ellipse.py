import cv2

image = cv2.imread("../data/test7.jpg")

image = cv2.ellipse(image, (0,135), (100,135), 0, 0, 360, (200, 30, 100), 2, cv2.LINE_AA, None)

cv2.imshow("adfd", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
