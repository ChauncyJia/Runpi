#配置修改刷新率
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
#刷新30frams → controls={"FrameDurationLimits":(33333,33333)}
#刷新25frams → controls={"FrameDurationLimits":(40000,40000)}
config = picam2.create_video_configuration(controls={"FrameDurationLimits":(33333,33333)})

print(config['controls'])