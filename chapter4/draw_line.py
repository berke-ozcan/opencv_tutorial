import cv2

image = cv2.imread("../data/test2.jpg")

image = cv2.line(image, (100, 100), (300, 200), (10, 230, 210), 5, cv2.LINE_AA, None)

cv2.imshow("asffds", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
