import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

for led in range(1,11):
	GPIO.output(7,GPIO.HIGH)
	sleep(1)
	GPIO.output(7,GPIO.LOW)
	sleep(1)

GPIO.cleanup()
