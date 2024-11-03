# 相机可以实现快速帧速率以在预览窗口中显示，但也可以切换到（较慢的帧速率）高分辨率捕获模式以获得最佳质量的图像。

from picamera2 import Picamera2,Preview
import time
picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(1)

#array
array = picam2.switch_mode_and_capture_array(capture_config,"main")
print(array)
# #PIL
PIL_data = picam2.switch_mode_and_capture_image(capture_config,"main")
print(PIL_data)
#file
picam2.switch_mode_and_capture_file(capture_config,"17.jpg")