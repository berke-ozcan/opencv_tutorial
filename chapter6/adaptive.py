import cv2

image = cv2.imread("../data/test1.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bw = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 299,20)

cv2.imshow("asdf", image)
cv2.imshow("xdxd", bw)

cv2.waitKey(0)
cv2.destroyAllWindows()