import cv2

image = cv2.imread("../data/test7.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
keypoint, descriptor = sift.detectAndCompute(image_gray, None)

image_keys = cv2.drawKeypoints(image, keypoint, None, (200, 40, 130))

cv2.imshow("dfsdfsd", image_keys)

cv2.waitKey(0)
cv2.destroyAllWindows()

