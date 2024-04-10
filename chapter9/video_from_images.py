import cv2
import os

fps = 60

writer = cv2.VideoWriter("xdxdxdasdxdxd.mp4", cv2.VideoWriter.fourcc(*'mp4v'), fps, (500, 500))

i = 1
while True:
    if not os.path.exists("../videotest/" + str(i) + ".jpg"):
        break
    frame = cv2.imread("../videotest/" + str(i) + ".jpg")
    frame = cv2.resize(frame, (500,500))
    cv2.imshow("xdxdxdxd", frame)
    writer.write(frame)
    i += 1
    if cv2.waitKey(3) == ord('q'):
        break

writer.release()
cv2.destroyAllWindows()

