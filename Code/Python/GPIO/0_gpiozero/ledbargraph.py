#硬件：RaspiberryPi 4B
#连接方式：GPIO4，5，6，13，19，26 ---  连接各个led一端
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，LED集合灯各自运行

from signal import pause
from gpiozero import LEDBarGraph
from time import sleep
#BCM编码
graph = LEDBarGraph(4, 5, 6, 13, 19, 26, )

graph.value = 1  # (1, 1, 1, 1, 1, 1)
sleep(1)
graph.value = 1/2  # (1, 1, 1, 0, 0, 0)
sleep(1)
graph.value = -1/2  # (0, 0, 0, 1, 1, 1)
sleep(1)
graph.value = 1/4  # (1, 0, 0, 0, 0, 0)
sleep(1)
graph.value = -1  # (1, 1, 1, 1, 1, 1)
sleep(1)