#硬件：RaspiberryPi 4B   对射传感器
#连接方式：BCM26 (board:pin37) ---  连接DO
#         GND OV (board:pin39) ---  连接GND
#         3V3 pin1 --- 连接VCC
#内容: 运行程序，物品经过对射口，计数，查看打印状态

from functools import partial
import RPi.GPIO as GPIO
from time import sleep


def interrupt_callback(pin_do):
    global count
    count += 1
    print(count)
pin_do = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_do, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pin_do,GPIO.RISING,interrupt_callback,200)

count = 0
while True:
    try:
        if GPIO.input(pin_do) == 0:
          None
        sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
GPIO.cleanup()