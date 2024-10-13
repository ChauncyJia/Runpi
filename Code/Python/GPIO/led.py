import RPi.GPIO as GPIO   #导入RPi的GPIO
from time import sleep

# 设置GPIO使用的编码格式
GPIO.setmode(GPIO.BCM)

# 设置BCM pin4 为输出模式
GPIO.setup(4,GPIO.OUT)

#设置 pin4 为高电平
GPIO.output(4,GPIO.HIGH)
sleep(5)  #延时

#设置 pin4 为低电平
GPIO.output(4,GPIO.LOW)
sleep(1)

#清理
GPIO.cleanup()