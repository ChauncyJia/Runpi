# 设置图像质量

from picamera2 import Picamera2,Preview
import time
picam2 = Picamera2()
#JPEG 质量级别，其中 0 表示最差质量，95 表示最佳质量
picam2.options["quality"] = 95
#PNG 压缩级别，其中 0 表示不压缩，1 表示实际执行任何压缩的最快，9 表示最慢
picam2.options["compress_level"] = 2
picam2.start()
time.sleep(1)
picam2.capture_file('20-1.jpg')
picam2.capture_file('20-2.png')

