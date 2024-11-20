import cv2
import time
from picamera2 import Picamera2
from libcamera import Transform

#显示图片等待5s后关闭
img = cv2.imread("face.bmp")
print(img.shape)
cv2.imshow("photo",img)
cv2.waitKey(5000) 

#播放5s的视频
vid_cap = cv2.VideoCapture("test.mp4")

start_time = time.time()
while True:
    success, vid = vid_cap.read()
    if success:
            cv2.imshow("Video",vid)
    if time.time() - start_time > 5:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(1/25)
vid_cap.release()

#播放5s的摄像头画面

picam2 = Picamera2()
config = picam2.create_video_configuration(main={"format":"RGB888","size":[720,500]},transform=Transform(hflip = 1))
picam2.configure(config)
picam2.start()
start_time = time.time()
while True:
    vid = picam2.capture_array()
    cv2.imshow("Video",vid)
    if time.time() - start_time > 5:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(1/25)


#播放ip 摄像头画面10s
ip_cam = "http://admin:123@192.168.31.15:8081"
vid_cap = cv2.VideoCapture(ip_cam)

start_time = time.time()
while True:
    success, vid = vid_cap.read()
    if success:
            cv2.imshow("Video",vid)
    if time.time() - start_time > 10:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(1/25)
vid_cap.release()
