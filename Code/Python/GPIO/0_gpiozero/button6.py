#硬件：RaspiberryPi 4B
#连接方式：GPIO17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#         GPIO4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容: 运行程序，持续按下按钮LED点闪烁，松手LED点亮，  键盘中断LED关闭

from gpiozero import Button, LED 
from time import sleep

button = Button(17)
led = LED(4)
while True:
    try:
        button.when_activated = led.blink
        button.when_deactivated = led.on
        sleep(0.1)
    except KeyboardInterrupt:
        print("User Quit")
        button.when_deactivated = led.off
        break