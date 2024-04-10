import cv2

image = cv2.imread("../data/test4.png")

image = cv2.resize(image, (500,500))

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray, 100, 200)

contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
image_cnt = cv2.drawContours(image, contours, -1, (100,230,40), 2, cv2.LINE_AA)

print(len(contours))

cv2.imshow("dsfsdfssdd", img_canny)
cv2.imshow("dsfsdfsd", image_cnt)

cv2.waitKey(0)
cv2.destroyAllWindows()