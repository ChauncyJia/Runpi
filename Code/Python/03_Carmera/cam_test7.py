#同时拍摄raw格式和jpg格式图片

import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview()

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

buffers, metadata = picam2.switch_mode_and_capture_buffers(capture_config,["main","raw"])
picam2.helpers.save(picam2.helpers.make_image(buffers[0], capture_config["main"]), metadata, "full.jpg")
picam2.helpers.save_dng(buffers[1],metadata, capture_config["raw"], "full.dng")