import cv2

image = cv2.imread("../data/balon.jpg")

image = cv2.resize(image, (250,250))

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray, 100, 200)

contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
image_cnt = cv2.drawContours(image, contours, -1, (100,230,40), 2, cv2.LINE_AA)

print(len(contours))

x, y, z, t = cv2.boundingRect(contours[0])
image_cnt = cv2.rectangle(image_cnt, (x,y), (x+z,y+t), (220,50,40), 2, cv2.LINE_AA, None)

(x,y), rad = cv2.minEnclosingCircle(contours[0])
image_cnt = cv2.circle(image_cnt, (int(x), int(y)), int(rad), (30, 30, 200), 3, cv2.LINE_AA, None)


cv2.imshow("dsfsdfssdd", img_canny)
cv2.imshow("dsfsdfsd", image_cnt)

cv2.waitKey(0)
cv2.destroyAllWindows()
