#对预览图像做翻转 hflip 左右 vflip 上下

# Run the camera with a 180 degree rotation.
import time

import libcamera

from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration()
preview_config["transform"] = libcamera.Transform(hflip=1, vflip=0)
picam2.configure(preview_config)

picam2.start()
time.sleep(5)