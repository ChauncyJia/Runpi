#硬件：RaspiberryPi 4B
#连接方式：GPIO17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#         GPIO4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容: 运行程序，按下按钮 LED点亮 释放按钮LED熄灭  键盘中断

from time import sleep
from gpiozero import Button, LED 

button = Button(17)
led = LED(4)
while True:
    try:
        led.source = button
        sleep(0.1)
    except KeyboardInterrupt:
        print("User Quit")
        break