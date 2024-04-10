import cv2

test1_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test1.jpg"
test2_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test2.jpg"
test3_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test3.png"
test4_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test4.png"
test5_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test5.png"
test6_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test6.png"
test7_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test7.jpg"

image = cv2.imread(test7_dir)

resized_image = cv2.resize(image, (200,700))
p144_image = cv2.resize(cv2.resize(image, (50,50)), (500,500))
p72_image = cv2.resize(cv2.resize(image, (10,10)), (500,500))

cv2.imwrite("sdasdsdsads.png", resized_image)

cv2.imshow("resized", resized_image)
cv2.imshow("144p", p144_image)
cv2.imshow("original", image)
cv2.imshow("even worse lol", p72_image)
cv2.imshow("wide", cv2.resize(image, (700,100)))

cv2.waitKey(0)
cv2.destroyAllWindows()


