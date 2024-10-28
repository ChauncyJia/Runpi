#硬件：RaspiberryPi 4B
#连接方式：BCM4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，小灯呼吸闪烁10次，键盘中断

from gpiozero import PWMLED

led = PWMLED(4)
#闪烁10次
led.pulse(1,1,10,False)
print("End")