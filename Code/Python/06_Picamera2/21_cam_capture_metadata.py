# 捕获元数据

from picamera2 import Picamera2,Metadata
import time
picam2 = Picamera2()
picam2.start()
time.sleep(1)
metadata = picam2.capture_metadata()
print(metadata)

print("-------------------------------------")
for key,value in metadata.items():
    print(f"{key}---{value}")

#  捕获元数据是将应用程序与相机帧同步的好方法（如果您实际上不需要帧）。
#对 capture_metadata （或实际上任何捕获函数）的第一次调用通常会立即返回
#因为 Picamera2 通常在内部保留最后一个相机图像。
#但之后，每个捕获调用都将等待新帧到达（除非应用程序等待了很长时间才发出图像再次已经存在的请求）。
picam2.start()
for i in range(30):
    metadata = picam2.capture_metadata()
    print("Frame",i ,'has arrived')


#object
metadata = Metadata(picam2.capture_metadata())
print(metadata.ExposureTime,metadata.AnalogueGain)