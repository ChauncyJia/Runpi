import RPi.GPIO as GPIO #导入RPi的GPIO
from time import sleep

# 设置GPIO使用的编码格式
GPIO.setmode(GPIO.BCM)
# 设置BCM pin4 为输出模式
GPIO.setup(4,GPIO.OUT)

#循环100次
for led in range(1, 101):
	#pin4 输出高
	GPIO.output(4,GPIO.HIGH)
	sleep(0.1)

	#pin4 输出低
	GPIO.output(4,GPIO.LOW)
	sleep(0.1)

#清理
GPIO.cleanup()
