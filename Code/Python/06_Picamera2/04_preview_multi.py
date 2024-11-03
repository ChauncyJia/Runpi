#预览窗口,请使用VNC图形界面运行
from picamera2 import Picamera2, Preview
from libcamera import Transform
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(main={"size":[1280,720]})
picam2.configure(camera_config)
picam2.start(show_preview=True)
time.sleep(2)

picam2.stop_preview()
picam2.start_preview(True)
time.sleep(2)