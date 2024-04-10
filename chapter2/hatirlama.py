import cv2

img_dir = "../data/test1.jpg"

image = cv2.imread(img_dir)

cropped = image[50:300, 100:250]
resized = cv2.resize(image, (150, 600))
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
blue, green, red = cv2.split(image)

'''

cv2.imshow("original", image)
cv2.imshow("resized xd", resized)
cv2.imshow("cropped", cropped)
cv2.imshow("rotated", rotated)
cv2.imshow("red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

cv2.imwrite("xdxd.jpg", red)






