#硬件：RaspiberryPi 4B
#连接方式：GPIO26 (board:pin37) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#内容: 运行程序，检测开关是否按下 键盘中断

from turtle import up
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP)
count_press = 0
while True:
    try:
        if GPIO.input(26) == 0:
            count_press += 1
            print(count_press)
            sleep(0.5)
        else:
            pass
    except KeyboardInterrupt:
        break

GPIO.cleanup()
