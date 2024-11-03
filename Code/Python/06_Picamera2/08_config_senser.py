#摄像头sensor_mode
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
pre_config = picam2.create_preview_configuration()
picam2.configure(pre_config)
print(picam2.sensor_modes)
for senser_modes in picam2.sensor_modes:
    print("\n")
    for key, value in senser_modes.items():
        print(f"{key}:{value}")
time.sleep(1)

print(picam2.camera_configuration()['raw'])
#format：           封装传感器格式。这可以在请求原始流时作为 “format” 传递。
#unpacked：         如果需要解压缩的原始图像，请使用此格式代替 Raw Stream。
#size:              传感器输出的分辨率。请求原始流时，可以将该值作为“大小”传递。
#fps:               该模式支持的最大帧速率
#bit_depth:         每个像素样本中的位数
#crop_limits：      全分辨率传感器输出中该模式的确切视野
#exposure_limits ： 该模式下允许的最大和最小曝光值（以微秒为单位）



# format:SRGGB10_CSI2P
# unpacked:SRGGB10
# bit_depth:10
# size:(1536, 864)
# fps:120.13
# crop_limits:(768, 432, 3072, 1728)
# exposure_limits:(9, 77208384, None)


# format:SRGGB10_CSI2P
# unpacked:SRGGB10
# bit_depth:10
# size:(2304, 1296)
# fps:56.03
# crop_limits:(0, 0, 4608, 2592)
# exposure_limits:(13, 112015443, None)


# format:SRGGB10_CSI2P
# unpacked:SRGGB10
# bit_depth:10
# size:(4608, 2592)
# fps:14.35
# crop_limits:(0, 0, 4608, 2592)
# exposure_limits:(26, 220417486, None)

