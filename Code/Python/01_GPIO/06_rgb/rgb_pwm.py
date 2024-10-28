#硬件：RaspiberryPi 4B  rgb灯模块
#连接方式：BCM17，16，13 ---  连接各个模块R,G,B
#         GND OV (board:pin39) ---  连接GND
#内容：运行程序，LED 显示依次显示颜色 

import RPi.GPIO as GPIO
from time import sleep

class RGBLED():

    def __init__(self,R_LED,G_LED,B_LED):
        """初始化RGB"""
        self.pins = [R_LED, G_LED, B_LED]
        #初始化电平
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        #设置pwm
        self.r_pwm = GPIO.PWM(R_LED,3000)
        self.g_pwm = GPIO.PWM(G_LED,3000)
        self.b_pwm = GPIO.PWM(B_LED,3000)
        #初始占空比
        self.r_pwm.start(0)
        self.g_pwm.start(0)
        self.b_pwm.start(0)

    def color2ration(self,x,max_color,max_ratio):
        """颜色(0-255)转为占空比(0-100)"""
        return x * max_ratio / max_color
    
    def setcolor(self,color):
        """颜色设置"""
        R_val,G_val,B_val= color
        R = self.color2ration(R_val, 255, 100)
        G = self.color2ration(G_val, 255, 100)
        B = self.color2ration(B_val, 255, 100)
        #改变占空比
        self.r_pwm.ChangeDutyCycle(R)
        self.g_pwm.ChangeDutyCycle(G)
        self.b_pwm.ChangeDutyCycle(B)

    def destroy(self):
        self.r_pwm.stop()
        self.g_pwm.stop()
        self.b_pwm.stop()
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)

if __name__ =="__main__":

    GPIO.setmode(GPIO.BCM)

    R_LED = 17
    G_LED = 16
    B_LED = 13
    led_color = RGBLED(R_LED,G_LED,B_LED)

    colors = [(255,0,0),(255,100,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(128,0,128)]
    lists =['红',"橙",'黄','绿','青','蓝','紫色']
while True:
    try:
      for list,color in zip(lists,colors):
          print(f"{list}:{color}")
          led_color.setcolor(color)
          sleep(2)
    except KeyboardInterrupt:
        print("User Quit.")
        break
led_color.destroy()
GPIO.cleanup()