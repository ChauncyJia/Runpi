#捕获原始
from email.policy import default
from picamera2 import Picamera2
from picamera2.encoders import Encoder
import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration(raw={},encode="raw")
picam2.configure(video_config)

encoder = Encoder()
output = "test.raw"

picam2.start_recording(encoder, output)
time.sleep(10)
picam2.stop_recording()
