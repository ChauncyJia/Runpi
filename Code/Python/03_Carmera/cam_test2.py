#预览并拍照 全分辨率
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_capture_file("test2.jpeg")
picam2.close()
