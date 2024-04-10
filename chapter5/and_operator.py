import cv2

image1 = cv2.imread("../data/test7.jpg")
image2 = cv2.imread("../data/test1.jpg")
image4 = cv2.imread("../data/test3.png")

image1 = cv2.resize(image1, (500,500))
image2 = cv2.resize(image2, (500,500))
image4 = cv2.resize(image4, (500,500))

print(image1.shape)

'''
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        image1[i, j, 0] = 255
        if 160 > image1[i, j, 0]/3 + image1[i, j, 1]/3 + image1[i, j, 2]/3:
            image1[i, j, 0] = 0
        image1[i, j, 1] = image1[i, j, 0]
        image1[i, j, 2] = image1[i, j, 0]
'''

image3 = cv2.bitwise_and(image1, image2)
image4 = cv2.bitwise_and(image4, image2)
image5 = cv2.bitwise_and(image2, image4)

'''cv2.imshow("dfderwsfs", image1)
cv2.imshow("dfdsdsffs", image2)
cv2.imshow("dfdscxvfs", image3)
cv2.imshow("dfsgsdf4gfdg", image4)
cv2.imshow("dfsgsdf5gfdg", image5)
'''

image6 = cv2.addWeighted(image1, 0.5, image2, 0.2, 0)
cv2.imshow("dfsfdfsdfsdfsdf", image6)

cv2.waitKey(0)
cv2.destroyAllWindows()
