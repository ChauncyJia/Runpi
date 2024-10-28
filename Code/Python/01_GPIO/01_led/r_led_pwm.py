#硬件：RaspiberryPi 4B
#连接方式：BCM19 (board:pin35) ---  连接小灯
#         GND OV (board:pin25) ---  连接小灯另一端
#内容: 运行程序，小灯闪烁


import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
pwm = GPIO.PWM(19,50)

while True:
    pwm.start(0)
    sleep(0.5)
    pwm.start(50)
    sleep(0.5)
    pwm.start(100)

GPIO.cleanup()