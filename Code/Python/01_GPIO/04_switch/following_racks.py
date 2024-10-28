#硬件：RaspiberryPi 4B   红外避障模块
#连接方式：BCM26 (board:pin37) ---  连接DO
#         GND OV (board:pin39) ---  连接GND
#         3V3 pin1 --- 连接VCC
#内容: 运行程序，移动传感器照-黑色和白色 ，白色时提示传感器偏离

import RPi.GPIO as GPIO
from time import sleep

pin_do = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_do, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    try:
        if GPIO.input(pin_do) == 1:
            None
        else:
            print("传感器已偏离")
        sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()