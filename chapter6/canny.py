import cv2

image = cv2.imread("../data/test1.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bw = cv2.Canny(image, 150, 256, None, 3, False)
#bw2 = cv2.Canny(image, 150, 256, None, 3, True)
#bw3 = cv2.bitwise_and(bw, bw2)

cv2.imshow("asdf", image)
cv2.imshow("xdxd", bw)
#cv2.imshow("xadxd", bw2)
#cv2.imshow("xasadsadxd", bw3)

cv2.waitKey(0)
cv2.destroyAllWindows()