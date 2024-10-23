import RPi.GPIO as GPIO  #GPIO#导入RPi的GPIO
from time import sleep

# 设置GPIO使用的编码格式
GPIO.setmode(GPIO.BCM)

# 设置BCM pin4/26 为输入模式
GPIO.setup(4,GPIO.IN)
GPIO.setup(26,GPIO.IN)

#读取pin的值
value_4 = GPIO.input(4) 
value_26  = GPIO.input(26)

#打印
print(value_4)
print(value_26)

#清理
GPIO.cleanup()
