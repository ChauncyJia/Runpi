# 捕获请求

from picamera2 import Picamera2,Metadata
import time


picam2 = Picamera2()
picam2.start()

request = picam2.capture_request()
request.save("main","23.jpg")

print(request.get_metadata())
request.release()
