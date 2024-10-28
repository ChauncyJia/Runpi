#硬件：RaspiberryPi 4B  无源蜂鸣器(低电平触发)
#连接方式：3_3V pin1 --- 连接蜂鸣器 VCC
#         BCM17 (board:pin11) ---  连接蜂鸣器I/O
#         GND OV (board:pin25) ---  连接蜂鸣器GND
#内容: 运行程序，蜂鸣器发声5s, 然后关闭，打印关闭蜂鸣器。

import RPi.GPIO as GPIO   #导入RPi的GPIO
from time import sleep

# 设置GPIO使用的编码格式
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)

GPIO.output(17,GPIO.HIGH)
sleep(1)

GPIO.output(17,GPIO.LOW)
print("buzzor on")
sleep(5)

GPIO.output(17,GPIO.HIGH)
print("buzzor off")

#清理
GPIO.cleanup()