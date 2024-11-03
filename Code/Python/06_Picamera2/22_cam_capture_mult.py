# 捕获多次

from picamera2 import Picamera2,Metadata
import time


picam2 = Picamera2()
config = picam2.create_preview_configuration(lores={"format":"RGB888"})
picam2.configure(config)

picam2.start()
(main, lores), metadata = picam2.capture_arrays(["main", "lores"])
time.sleep(1)
print(main)
print(lores)

# picam2.helpers.make_array   从平面 1d 数组（例如由 capture_buffer 返回）创建 2d（或 3d，允许多个颜色通道）数组
# picam2.helpers.make_image   从平面 1d 数组制作 PIL 图像（例如，由 capture_buffer 返回）
# picam2.helpers.save         将 PIL 图像保存到文件
# picam2.helpers.save_dng     将 PIL 图像保存到 DNG 文件

(buffer1,buffer2), metadata = picam2.capture_buffers(["main","lores"])
img1 = picam2.helpers.make_image(buffer1,picam2.camera_configuration()["main"])
picam2.helpers.save(img1, metadata, '22.jpg')
img2 = picam2.helpers.make_image(buffer2,picam2.camera_configuration()["lores"])
picam2.helpers.save(img2, metadata, '21.jpg')