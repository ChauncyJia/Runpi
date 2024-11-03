# 通过object
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.configure('preview')

# 在相机启动前设置
picam2.controls.ExposureTime = 10000
picam2.controls.AnalogueGain = 1.0
picam2.start() 

# 在相机启动后设置
picam2.start() 
with picam2.controls as controls:
    controls.ExPosureTime = 10000
    controls.AnalogueGain = 1.0