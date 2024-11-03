#多张合成来降噪
from picamera2 import Picamera2, Preview
import time
import numpy as np
from PIL import Image

picam2 = Picamera2()
picam2.start_preview()
capture_config = picam2.create_still_configuration()
picam2.configure(capture_config)

picam2.start()
time.sleep(2)

with picam2.controls as ctrl:
    ctrl.AnalogueGain = 1.0
    ctrl.ExposureTime = 250000
time.sleep(2)

imgs = 3
sumv = None

for i in range(imgs):
    if sumv is None:
        sumv = np.longdouble(picam2.capture_array())
        img = Image.fromarray(np.uint8(sumv))
        img.save("original.tif")
    else:
        sumv += np.longdouble(picam2.capture_array())

img = Image.fromarray(np.uint8(sumv / imgs))
img.save("averaged.tif")