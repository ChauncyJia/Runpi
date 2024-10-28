#硬件：RaspiberryPi 4B
#连接方式：BCM4 (board:pin7) ---  连接led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，小灯点亮 1s后小灯熄灭 循环10次

from gpiozero import LED #导入 gpiozero库的LED
from time import sleep
#BCM编码
led = LED(4)
for count in range(1,11):
    led.on()
    sleep(1)
    led.off()
    sleep(1)


#以下均为同一引脚
# led = LED(4)
# led = LED("GPIO4")
# led = LED("BCM4")
# led = LED("BOARD7")
# led = LED("WPI7")
# led = LED("J8:11")