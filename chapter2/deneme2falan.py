import cv2

test1_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test1.jpg"
test2_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test2.jpg"
test3_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test3.png"
test4_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test4.png"
test5_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test5.png"
test6_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test6.png"
test7_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test7.jpg"

image1 = cv2.imread(test7_dir)
image2 = cv2.imread(test2_dir)

for i in range(0, image1.shape[0]):
    for j in range(0, image1.shape[1]):
        for k in range(0, 3):
            image1[i, j, k] = (image1[i, j, k]/3)*2 + image2[i, j, k]/3


image1 = cv2.resize(image1, (900, 600))

cv2.imwrite("xdasdweqwerasd.jpg", image1)

cv2.imshow("asfasdasddf", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()


