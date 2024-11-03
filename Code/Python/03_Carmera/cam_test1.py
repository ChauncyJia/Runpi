#拍照 指定大小800x600
from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(camera_config)
picam2.start_preview()
picam2.start()
sleep(2)
picam2.capture_file("test1.jpg")
picam2.close()