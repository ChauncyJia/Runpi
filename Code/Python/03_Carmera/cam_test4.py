#不预览连续拍3张照片
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_capture_files("test4-{:d}.jpeg",show_preview=False,num_files=3,delay=0.5)
