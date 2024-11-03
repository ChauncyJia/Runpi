#同时拍摄raw格式和jpg格式图片简单方法

import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview()

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

r = picam2.switch_mode_capture_request_and_stop(capture_config)
r.save("main","full2.jpg")
r.save_dng("full2.dng")