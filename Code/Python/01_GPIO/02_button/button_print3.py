#硬件：RaspiberryPi 4B
#连接方式：BCM17 (board:pin11) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#内容: 按下开关显示hello，释放开关显示goodbye 键盘中断

from gpiozero import Button   
from time import sleep

def say_hello():
    print("hello!")

def say_goodbye():
    print("good bye!")

button =Button(17)
while True:
    try:
        button.when_activated = say_hello
        button.when_deactivated= say_goodbye
        sleep(0.1)
    except KeyboardInterrupt:
        print("User Quit.")
        break
