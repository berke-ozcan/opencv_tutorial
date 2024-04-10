import cv2

image = cv2.imread("../data/test1.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh, bw = cv2.threshold(image, 150, 0, cv2.THRESH_TOZERO_INV)

print(thresh)
cv2.imshow("asdf", image)
cv2.imshow("xdxd", bw)

cv2.waitKey(0)
cv2.destroyAllWindows()