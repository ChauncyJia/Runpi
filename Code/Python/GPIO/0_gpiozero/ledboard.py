#硬件：RaspiberryPi 4B
#连接方式：GPIO4，5，6，13，19，26 ---  连接各个led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，LED集合灯打开，关闭，闪烁 循环

from gpiozero import LEDBoard
from time import sleep
#BCM编码
leds = LEDBoard(4, 5, 6, 13, 19, 26)
while True:
    try:
        leds.on()
        sleep(1)
        leds.off()
        sleep(1)
        leds.value = (1, 0, 1, 0, 1, 1)
        sleep(1)
        leds.blink()
        sleep(1)
    except KeyboardInterrupt:
        break
