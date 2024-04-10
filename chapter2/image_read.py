import time

import cv2

test1_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test1.jpg"
test2_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test2.jpg"
test3_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test3.png"
test4_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test4.png"
test5_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test5.png"
test6_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test6.png"
test7_dir = "C:/ProjectFiles/PyCharm/OpenCV_Tutorials_FV/pythonProject/data/test7.jpg"

image = cv2.imread(test1_dir, -1)

print(image.shape)

cv2.imshow("qweqwewqeqw",image)
cv2.waitKey(0)





