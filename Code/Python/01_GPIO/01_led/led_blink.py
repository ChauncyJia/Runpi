#硬件：RaspiberryPi 4B
#连接方式：BCM4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，小灯循环闪烁10次

from gpiozero import LED #导入 gpiozero库的LED

#BCM编码
led = LED(4)
led.blink(1,1,10,False)
print("End")