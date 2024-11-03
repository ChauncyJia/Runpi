# Camera controls 参数
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
#配置方法-相机启动前
""" preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.set_controls({"ExposureTime": 10000, "AnalogueGain": 1.0}))
picam2.start() """

#配置方法-相机启动后
""" preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start() 
picam2.set_controls({"ExposureTime": 10000, "AnalogueGain": 1.0}))
"""


#查看参数
for key, value in picam2.camera_controls.items():
    print(f"{key}:{value}")

# 控件名：(min, max, default)

# AfRange:(0, 2, 0)
# LensPosition:(0.0, 32.0, 1.0)
# AfMetering:(0, 1, 0)
# CnnEnableInputTensor:(False, True, False)
# AfTrigger:(0, 1, 0)
# AeFlickerPeriod:(100, 1000000, None)
# AwbMode:(0, 7, 0)
# AeConstraintMode:(0, 3, 0)
# AfPause:(0, 2, 0)
# Contrast:(0.0, 32.0, 1.0)
# ColourGains:(0.0, 32.0, None)
# ExposureValue:(-8.0, 8.0, 0.0)
# Saturation:(0.0, 32.0, 1.0)
# HdrMode:(0, 4, 0)
# AwbEnable:(False, True, None)
# ScalerCrop:((0, 0, 0, 0), (65535, 65535, 65535, 65535), (0, 0, 0, 0))
# AeFlickerMode:(0, 1, 0)
# Sharpness:(0.0, 16.0, 1.0)
# AnalogueGain:(1.0, 16.0, None)
# NoiseReductionMode:(0, 4, 0)
# ExposureTime:(0, 66666, None)
# AeEnable:(False, True, None)
# ScalerCrops:((0, 0, 0, 0), (65535, 65535, 65535, 65535), (0, 0, 0, 0))
# Brightness:(-1.0, 1.0, 0.0)
# FrameDurationLimits:(33333, 120000, None)
# AeMeteringMode:(0, 3, 0)
# StatsOutputEnable:(False, True, False)
# AfMode:(0, 2, 0)
# AfWindows:((0, 0, 0, 0), (65535, 65535, 65535, 65535), (0, 0, 0, 0))
# AeExposureMode:(0, 3, 0)
# AfSpeed:(0, 1, 0)