#硬件：RaspiberryPi 4B   水滴传感器
#连接方式：BCM26 (board:pin37) ---  连接S
#         GND OV (board:pin39) ---  连接-
#         3V3 pin1 --- 连接+
#内容: 运行程序，将水滴滴在传感器金属板上，查看打印状态

import RPi.GPIO as GPIO
from time import sleep

pin_do = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_do, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    try:
        if GPIO.input(pin_do) == 1:
            print("有水出没了")
        else:
            None
        sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()