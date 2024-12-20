#拍照相关的config
import time

from picamera2 import Picamera2

picam2 = Picamera2()

# We don't really need to change anyhting, but let's mess around just as a test.
picam2.preview_configuration.size = (800, 600)
picam2.preview_configuration.format = "YUV420"
picam2.still_configuration.size = (1600, 1200)
picam2.still_configuration.enable_raw()
picam2.still_configuration.raw.size = picam2.sensor_resolution

picam2.start("preview", show_preview=True)
time.sleep(2)

picam2.switch_mode_and_capture_file("still", "test17.jpg")
