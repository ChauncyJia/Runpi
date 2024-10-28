#硬件：RaspiberryPi 4B   PIR人体热释放传感器
#连接方式：BCM26 (board:pin37) ---  连接DO(中)
#         GND OV (board:pin39) ---  连接(右)
#         3V3 pin1 --- 连接VCC(左)
#内容: 运行程序，触摸传感器，查看打印状态

import RPi.GPIO as GPIO
from time import sleep

pin_do = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_do, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    try:
        if GPIO.wait_for_edge(pin_do,GPIO.RISING):
            print("有人来了")
        else:
            None
        sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()