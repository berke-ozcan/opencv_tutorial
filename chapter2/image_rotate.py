import cv2

test1_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test1.jpg"
test2_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test2.jpg"
test3_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test3.png"
test4_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test4.png"
test5_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test5.png"
test6_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test6.png"
test7_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test7.jpg"

image = cv2.imread(test7_dir)
i2 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
i3 = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("asdsdasasd", image)
cv2.imshow("asdsdadsfsasd", i2)
cv2.imshow("asdsdassasd", cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE))
cv2.imshow("asdsdaserasd", i3)

cv2.waitKey(0)
cv2.destroyAllWindows()


