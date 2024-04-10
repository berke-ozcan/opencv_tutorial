import cv2

video_path = "../data/superidol.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

writer = cv2.VideoWriter("xdxdxdasdxdxd.mp4", cv2.VideoWriter.fourcc(*'mp4v'), fps*2, (700, 200))

while True:
    ret, frame = cap.read()
    if ret is True:
        frame = frame[:,480:800]
        frame = cv2.resize(frame, (700,200))
        cv2.imshow("xdxdxdxd", frame)
        writer.write(frame)
    else:
        break
    if cv2.waitKey(3) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

