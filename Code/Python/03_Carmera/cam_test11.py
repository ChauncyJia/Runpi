#对camera的拍摄参数进行修改然后拍照保存 -简单方法1
import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(1)

controls = {"AwbEnable":0, "AeEnable":0}
picam2.set_controls(controls)
time.sleep(5)

picam2.capture_file("test11.jpg")
picam2.close()
