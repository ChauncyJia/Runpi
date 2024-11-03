#预览窗口,请使用VNC图形界面运行
from picamera2 import Picamera2, Preview
from libcamera import Transform
import time

picam2 = Picamera2()
# xy：预览位置 以下配置只修改预览 不影响实际图像
picam2.start_preview(Preview.QTGL,x=500, y=200, width=800, height=600,transform = Transform(hflip=1,vflip=0))
picam2.start()
time.sleep(2)

picam2.stop_preview()
picam2.start_preview(True)
time.sleep(2)