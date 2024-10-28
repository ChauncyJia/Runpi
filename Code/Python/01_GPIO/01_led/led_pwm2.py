#硬件：RaspiberryPi 4B
#连接方式：BCM4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，小灯从最暗逐渐变亮 键盘中断

from gpiozero import PWMLED
from time import sleep

led = PWMLED(4)
while True:
    try:
        for value in range(1,10):
            led.value = value * 0.1
            sleep(0.2)
    except KeyboardInterrupt:
        print("User Quit.")
        break