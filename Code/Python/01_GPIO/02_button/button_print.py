#硬件：RaspiberryPi 4B
#连接方式：GPIO17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#内容: 运行程序，检测开关是否按下 键盘中断

from gpiozero import Button   
from time import sleep

button = Button(17)
while True:
    try:
        if button.is_pressed:
            print("按钮按下")
        else:
            print("按钮释放")
        sleep(0.5)
    except KeyboardInterrupt:
        print("User Quit.")
        break