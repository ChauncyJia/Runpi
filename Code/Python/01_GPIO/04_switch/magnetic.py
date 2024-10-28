#硬件：RaspiberryPi 4B   干簧管磁控传感器
#连接方式：BCM26 (board:pin37) ---  连接DO
#         GND OV (board:pin39) ---  连接GND
#         3V3 pin1 --- 连接VCC
#内容: 运行程序，磁体靠近和远离传感器 查看状态。

import RPi.GPIO as GPIO
from time import sleep

pin_do = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_do, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    try:
        if GPIO.input(pin_do) == 0:
            print("有磁铁靠近")
        else:
            None
        sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()