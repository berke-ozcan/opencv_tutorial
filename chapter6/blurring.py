import cv2

image = cv2.imread("../data/test1.jpg")

img_gauss = cv2.GaussianBlur(image, (11,11), 0)
img_gauss_with_sigma = cv2.GaussianBlur(image, (11,11), 1)
img_median = cv2.medianBlur(image, 11)
img_blur = cv2.blur(image, (11,11))

cv2.imshow("original", image)
cv2.imshow("gauss", img_gauss)
cv2.imshow("gauss with sigma", img_gauss_with_sigma)
cv2.imshow("median", img_median)
cv2.imshow("blur", img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
