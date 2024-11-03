#连续拍摄多张照片
from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.configure("still")
picam2.start()

time.sleep(1)
picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0})
time.sleep(1)

start_time = time.time()
for i in range(1, 5):
    r = picam2.capture_request()
    r.save("main",f"test5-{i}.jpg")
    r.release()
    print(f"Captured image {i} of 4 at {time.time() - start_time:.2f}s")

picam2.stop()