import cv2

image = cv2.imread("../data/test3.png")

image = cv2.rectangle(image, (100, 100), (300, 200), (10, 230, 0), 2, cv2.LINE_AA, None)

cv2.imshow("asffds", image)

cv2.waitKey(0)
cv2.destroyAllWindows()