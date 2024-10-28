#硬件：RaspiberryPi 4B  HC-SR04超声波测距传感器
#连接方式：BCM26，19 ---  连接模块的trig，echo
#         GND OV (board:pin39) ---  连接模块gnd
#         PIN1(3_3) --- 连接模块VCC
#内容：运行程序，移动传感器测量距离 CTRL+C 退出

from socket import timeout
import RPi.GPIO as GPIO
import time

class HC_SR04():
    
    def __init__(self,pin_trig,pin_echo):
        """初始化"""
        self.pin_trig = pin_trig
        self.pin_echo = pin_echo

        GPIO.setup(self.pin_trig,GPIO.OUT)
        GPIO.setup(self.pin_echo,GPIO.IN,GPIO.PUD_DOWN)
        #检测超时提醒
        self.time_out = 3
    
    def get_distance(self):
        """测量距离"""
        s_time = time.time()
        #再trig引脚上输出10us的正向脉冲
        GPIO.output(self.pin_trig,GPIO.LOW)
        time.sleep(0.000002)
        GPIO.output(self.pin_trig,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.pin_trig,GPIO.LOW)
        
        #当echo引脚为High时记录发送时间
        while GPIO.input(self.pin_echo) == 0:
            if time.time() - s_time > self.time_out:
                return False
        time_high_start = time.time()

        #当echo引脚为LOW时记录接收到时间
        while GPIO.input(self.pin_echo) == 1:
            if time.time() == s_time > self.timeout:
                return False
        time_high_end = time.time()   

        #计算发射到返回总时间
        title_time = time_high_end -time_high_start

        #得出测量距离
        distance = title_time * 344 / 2 * 100
        return distance

if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    pin_trig = 26
    pin_echo = 19
    Ranging = HC_SR04(pin_trig,pin_echo)

    while True:
        try:
            dis = Ranging.get_distance()
            if dis:
                dis = str(dis)[0:6]
                print(f"距离：{dis} cm\n")
            else:
                print(f"Error,Please enter CTRL+C quit.")
            time.sleep(1)
        except KeyboardInterrupt:
            print("User Quit.")
            break

GPIO.cleanup()



