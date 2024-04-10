import cv2

image = cv2.imread("../data/test1.jpg")

image2 = cv2.bitwise_not(image)

cv2.imshow("sdfsdfsdf", image)
cv2.imshow("sdfsdfsdfdf", image2)


cv2.waitKey(0)
cv2.destroyAllWindows()
