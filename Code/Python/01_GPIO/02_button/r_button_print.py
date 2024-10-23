#硬件：RaspiberryPi 4B
#连接方式：GPIO17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#内容: 运行程序，检测开关是否按下 键盘中断

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    try:
        if GPIO.input(17) == 0:
            print("按钮按下")
        else:
            print("按钮释放")
        sleep(0.1)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()