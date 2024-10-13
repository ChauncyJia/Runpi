from gpiozero import LED #导入 gpiozero库的LED
from time import sleep

#定义led BCM编码
led = LED(4)

for count in range(1,11):
    # 高电平
    led.on()
    sleep(1)
    # 低电平
    led.off()
    sleep(1)