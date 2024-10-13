import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

for led in range(1, 100):
	GPIO.output(4,GPIO.HIGH)
	sleep(0.1)
	GPIO.output(4,GPIO.LOW)
	sleep(0.1)

GPIO.cleanup()
