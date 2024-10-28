#硬件：RaspiberryPi 4B  rgb灯模块
#连接方式：BCM17，16，13 ---  连接各个模块R,G,B
#         GND OV (board:pin39) ---  连接led另一端
#内容：运行程序，LED 显示 红，绿，蓝 交替点亮 

import RPi.GPIO as GPIO
from time import sleep

R_LED = 17
G_LED = 16
B_LED = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(R_LED,GPIO.OUT)
GPIO.setup(G_LED,GPIO.OUT)
GPIO.setup(B_LED,GPIO.OUT)

while True:
    try:
        GPIO.output(R_LED,GPIO.HIGH)
        sleep(1)
        GPIO.output(R_LED,GPIO.LOW)
        sleep(1)
        GPIO.output(G_LED,GPIO.HIGH)
        sleep(1)
        GPIO.output(G_LED,GPIO.LOW)
        sleep(1)
        GPIO.output(B_LED,GPIO.HIGH)
        sleep(1)
        GPIO.output(B_LED,GPIO.LOW)
        sleep(1)
    except KeyboardInterrupt:
        print("User Quit.")
        break

GPIO.cleanup()