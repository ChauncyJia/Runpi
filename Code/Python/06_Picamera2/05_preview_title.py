#预览窗口的标题修改
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start(show_preview=True)

picam2.title_fields=["ExposureTime","AnalogueGain"]


time.sleep(5)