import RPi.GPIO as GPIO#导入RPi的GPIO
from time import sleep

# 设置GPIO使用的编码格式
GPIO.setmode(GPIO.BOARD)
# 设置Board pin7 为输出模式
GPIO.setup(7,GPIO.OUT)

#循环10次
for led in range(1,11):
	#pin7 输出高
	GPIO.output(7,GPIO.HIGH)
	sleep(1)
	#pin7 输出低
	GPIO.output(7,GPIO.LOW)
	sleep(1)

#清理
GPIO.cleanup()
