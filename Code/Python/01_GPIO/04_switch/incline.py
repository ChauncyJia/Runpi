#硬件：RaspiberryPi 4B   倾斜传感器
#连接方式：BCM26 (board:pin37) ---  连接DO
#         GND OV (board:pin39) ---  连接GND
#         3V3 pin1 --- 连接VCC
#内容: 运行程序，水平或倾斜传感器，查看打印状态

import RPi.GPIO as GPIO
from time import sleep

pin_do = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_do, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    try:
        if GPIO.input(pin_do) == 0:
            print("倾斜状态")
        else:
            print("水平状态")
        sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()