# 相机属性，无法改变

from picamera2 import Picamera2

picam2 = Picamera2()

print(picam2.camera_properties)
for key, value in picam2.camera_properties.items():
    print(f"{key}-----{value}")


# Model-----imx708
# UnitCellSize-----(1400, 1400)
# ColorFilterArrangement-----0
# Location-----2
# Rotation-----180
# PixelArraySize-----(4608, 2592)
# PixelArrayActiveAreas-----[(16, 24, 4608, 2592)]
# ScalerCropMaximum-----(0, 0, 0, 0)
# SystemDevices-----(20753, 20754, 20755, 20756, 20757, 20758, 20759, 20739, 20740, 20741, 20742)