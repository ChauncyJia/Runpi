#不预览只拍照
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_capture_file("test3.jpeg",show_preview=False,delay=0.5)
