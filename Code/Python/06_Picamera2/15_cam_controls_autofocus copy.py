# 自动对焦  camera V3
# 三种模式 通过读取：AfState
# Manual ：    镜头永远不会自发移动，但可以使用 “LensPosition” 控件来移动镜头【距离单位m】 0表示无穷大
# Auto :       “AfTrigger”控件可用于启动自动对焦周期。可以检查随图像接收的“AfState”元数据，
# Continuous : 自动对焦算法将持续运行，并在必要时自发重新聚焦。

from time import sleep
from picamera2 import Picamera2, Preview
from libcamera import controls

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()

#连续自动对焦
""" picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
sleep(10) """

#手动无穷
""" picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0})
sleep(10) """

#自动触发
job = picam2.autofocus_cycle(wait=False)
sucess = picam2.wait(job)
print(sucess)
sleep(10)