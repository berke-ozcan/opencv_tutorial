import cv2

video_dir = "../data/mae.mp4"

video_capture = cv2.VideoCapture(video_dir)

i = 1

while True:
    ret, frame = video_capture.read()
    if ret is True:

        # save frame to a directory here, file name is the variable i
        cv2.imwrite("../videotest/" + str(i) + ".jpg", frame)
        # i++
        i += 1

        cv2.imshow("xdxd", frame)
    else:
        break
    if cv2.waitKey(2) == ord('w'):
        break

cv2.destroyAllWindows()
video_capture.release()
