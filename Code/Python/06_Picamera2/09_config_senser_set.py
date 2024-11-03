#摄像头sensor_mode 设置
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

mode = picam2.sensor_modes[0]
pre_config = picam2.create_preview_configuration(sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']})

picam2.configure(pre_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

time.sleep(5)

