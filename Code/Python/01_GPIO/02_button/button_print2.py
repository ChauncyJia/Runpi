#硬件：RaspiberryPi 4B
#连接方式：BCM17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#内容: 按下开关，屏幕显示信息 键盘中断

from gpiozero import Button   
from time import sleep

button = Button(17)
while True:
    try:
        button.wait_for_active()
        print("按钮按下")
        sleep(0.1)
    except KeyboardInterrupt:
        print("User Quit.")
        break