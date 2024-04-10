import cv2

image = cv2.imread("../data/test7.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread("../data/test7b.jpg")
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
keypoint, descriptor = sift.detectAndCompute(image_gray, None)
keypoint2, descriptor2 = sift.detectAndCompute(image2_gray, None)

bf = cv2.BFMatcher()
matches = bf.match(descriptor, descriptor2)
matches = sorted(matches, key=lambda x: x.distance)
image_matcher = cv2.drawMatches(image, keypoint, image2, keypoint2, matches[:30], None)

cv2.imshow("safdsafdsasd", image_matcher)

cv2.waitKey(0)
cv2.destroyAllWindows()

