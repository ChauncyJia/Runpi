#将图像数据捕获到buffer
import time
import io
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start()

time.sleep(1)
data = io.BytesIO()
picam2.capture_file(data, format='jpeg')
print(data.getbuffer().nbytes)

time.sleep(1)
data = io.BytesIO()
picam2.switch_mode_and_capture_file(capture_config,data,format='jpeg')
print(data.getbuffer().nbytes)