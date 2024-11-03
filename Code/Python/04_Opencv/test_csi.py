import cv2
import numpy as np
import libcamera
from time import sleep
from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_preview_configuration(main = {"format":'RGB888',"size":(1280,720)},
                                             raw={"format":'SRGGB12',"size":(4608,2592)})
config["transform"] = libcamera.Transform(hflip = 1,vflip = 0)
picam2.configure(config)
picam2.start()

while True:
    frame = picam2.capture_array()
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    sleep(0.01)
cv2.destroyAllWindows()