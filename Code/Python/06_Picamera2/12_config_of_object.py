# config 通过object方式

from time import sleep
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
#配置
""" picam2.preview_configuration.main.size = (1920,1080)
picam2.configure("preview")
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(3)
picam2.stop_preview()
"""
#配置lores,
""" print("------------------------")
picam2.preview_configuration.enable_lores()
picam2.preview_configuration.lores.size = (320, 240)
picam2.configure("preview")
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(3)
picam2.stop_preview() """

#配置raw 失败可能和pi5相关
print("------------------------")
picam2.preview_configuration.enable_raw()
picam2.preview_configuration.raw.size = (1332, 990)
picam2.preview_configuration.raw.format = "SBGGR10"
picam2.configure("preview")
print(f"--{picam2.preview_configuration.raw}")
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(3)
picam2.stop_preview()
