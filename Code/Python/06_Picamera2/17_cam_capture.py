# 捕获

from picamera2 import Picamera2
import time
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())
picam2.start()
time.sleep(1)
#array
array = picam2.capture_array("main")
print(array)
#PIL
PIL_data = picam2.capture_image("main")
print(PIL_data)
#file
picam2.capture_file("17.jpg")