import cv2

video_path = "../data/mae.mp4"
cap = cv2.VideoCapture(video_path)

video_path2 = "../data/dw.mp4"
cap2 = cv2.VideoCapture(video_path2)

video_path3 = "../data/johnnybravo.mp4"
cap3 = cv2.VideoCapture(video_path3)

image = cv2.imread("../data/test1.jpg")
image = cv2.resize(image, (100,100))

fps = cap.get(cv2.CAP_PROP_FPS)

writer = cv2.VideoWriter("xdxdadxd.mp4", cv2.VideoWriter.fourcc(*'mp4v'), fps*2, (500, 500))

while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    if ret is True and ret2 is True and ret3 is True:
        frame2 = cv2.resize(frame2, (200,200))
        frame = cv2.resize(frame, (500,500))
        frame3 = cv2.resize(frame3, (150,50))

        frame[10:210, 200:400] = frame2
        frame[410:460, 40:190] = frame3
        frame[340:440, 300:400] = image

        cv2.imshow("xdxdxdxd", frame)
        writer.write(frame)
    else:
        break
    if cv2.waitKey(3) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

