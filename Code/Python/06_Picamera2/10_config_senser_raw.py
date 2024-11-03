#摄像头sensor_mode 修改sensor_mode 原始流配置将始终从给定传感器配置的传感器配置中为您填写
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

mode = picam2.sensor_modes[0]
pre_config = picam2.create_preview_configuration(raw={'format': 'SRGGB12',"size":(1332, 990)},
                                                sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']})

picam2.configure(pre_config)
print(picam2.camera_configuration()['raw'])
print(picam2.camera_configuration()['sensor'])
picam2.start_preview(Preview.QTGL)
picam2.start()

time.sleep(5)

