#通过align_configuration调整最佳
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
pre_config = picam2.create_preview_configuration({"size":(808,606)})
picam2.configure(pre_config)
print(pre_config["main"])
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(3)
picam2.stop_preview()
time.sleep(2)
picam2.align_configuration(pre_config)
print(pre_config["main"])
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(5)