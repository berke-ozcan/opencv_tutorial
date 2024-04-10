import cv2

video_dir = "../data/mae.mp4"

video_capture = cv2.VideoCapture(video_dir)

while True:
    ret, frame = video_capture.read()
    if ret is True:
        cv2.imshow("xdxd", frame)
    else:
        break
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    low_quality = cv2.resize(cv2.resize(frame, (70,70)), (720,480))
    cv2.imshow("rot", rotated_frame)
    cv2.imshow("144p", low_quality)
    if cv2.waitKey(2) == ord('w'):
        break

cv2.destroyAllWindows()
video_capture.release()
