#对camera的拍摄参数进行修改然后拍照保存 -简单方法2
import time
from picamera2 import Picamera2, Preview, controls

picam2 = Picamera2()
picam2.start_preview()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(1)

with picam2.controls as ctrl:
    ctrl.AnalogueGain = 6.0
    ctrl.ExposureTime = 60000
time.sleep(2)

ctrls = controls.Controls(picam2)
ctrls.AnalogueGain = 1.0
ctrls.ExposureTime = 10000
picam2.set_controls(ctrls)

time.sleep(2)

picam2.capture_file("test12.jpg")

picam2.close()