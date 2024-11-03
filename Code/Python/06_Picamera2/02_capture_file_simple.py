#预览分辨率拍摄照片，视频的简单方法（全分辨率）
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_capture_file("02.jpg",show_preview=False)  #SSH:show_preview = False

picam2.start_and_capture_files("02_{:d}.jpg",num_files=3,delay=0.5,show_preview=False) 

picam2.start_and_record_video("02.mp4",duration=5)