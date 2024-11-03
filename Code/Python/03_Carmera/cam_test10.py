#对camera的拍摄参数进行修改然后拍照保存(获取当前参数再写入，实际未改变)
import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(1)

metadata = picam2.capture_metadata()
print(f"metadata: {metadata}")
controls = {c: metadata[c] for c in ["ExposureTime", "AnalogueGain", "ColourGains"]}
print(controls)

picam2.set_controls(controls)
time.sleep(5)

picam2.capture_file("test10.jpg")
picam2.close()
