# 相机可以实现快速帧速率以在预览窗口中显示，但也可以切换到（较慢的帧速率）高分辨率捕获模式以获得最佳质量的图像。

from picamera2 import Picamera2,Preview
import time
picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
preview_config = picam2.create_preview_configuration()
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(1)
picam2.switch_mode(capture_config)
picam2.capture_file('19.jpg')
picam2.switch_mode(preview_config)
time.sleep(4)

