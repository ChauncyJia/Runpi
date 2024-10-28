#硬件：RaspiberryPi 4B
#连接方式：BCM17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#         GPIO4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容: 运行程序，按下按钮 LED点亮 释放按钮LED熄灭  键盘中断

from gpiozero import Button, LED 
from time import sleep

button = Button(17)
led = LED(4)
while True:
    try:
        button.when_activated = led.on
        button.when_deactivated = led.off
        sleep(0.1)
    except KeyboardInterrupt:
        print("User Quit")
        break