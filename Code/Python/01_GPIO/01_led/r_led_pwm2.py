#硬件：RaspiberryPi 4B
#连接方式：GPIO19 (board:pin35) ---  连接小灯
#         GND OV (board:pin25) ---  连接小灯另一端
#内容: 运行程序，小灯闪烁


import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
pwm = GPIO.PWM(19,50)

while True:
    try:
        for led in range(101):
            pwm.start(led)
            print(f"add: {led}")
            sleep(0.01)
        sleep(1)
        for led in range(101):
            count = 100
            led = count - led
            pwm.start(led)
            print(f"reduce: {led}")
            sleep(0.01)
        sleep(1)
    except KeyboardInterrupt:
        break

GPIO.cleanup()