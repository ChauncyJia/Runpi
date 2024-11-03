#预览分辨率拍摄一张照片
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview()   #Preview=DRM ,Preview=QTGL
picam2.start()
time.sleep(1)
picam2.capture_file("01.jpg")