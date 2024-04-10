import cv2

image = cv2.imread("../data/test7.jpg")

image = cv2.resize(image, (500,500))
image = cv2.putText(image, "xdxdxd", (0,500), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (200, 0, 0), 2, cv2.LINE_AA, None)
image = cv2.putText(image, "xdxdxd", (110,110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 200, 0), 2, cv2.LINE_AA, None)
image = cv2.putText(image, "xdxdxd", (120,120), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (200, 200, 0), 2, cv2.LINE_AA, None)
image = cv2.putText(image, "xdxdxd", (130,130), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 200), 2, cv2.LINE_AA, None)
image = cv2.putText(image, "xdxdxd", (140,140), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (200, 0, 200), 2, cv2.LINE_AA, None)
image = cv2.putText(image, "xdxdxd", (150,150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 200, 200), 2, cv2.LINE_AA, None)

cv2.imshow("xd", image)

cv2.imwrite("xdxdxdrainbow.png", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

