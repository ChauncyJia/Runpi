import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN)
GPIO.setup(26,GPIO.IN)

value_4 = GPIO.input(4)
value_26  = GPIO.input(26)

sleep(1)
print(value_4)
sleep(2)
print(value_26)

GPIO.cleanup()
