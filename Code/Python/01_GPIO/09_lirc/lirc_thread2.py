#硬件：RaspiberryPi 4B  + 红外接收模块
#连接方式： pin1(3_3V) --- 红外 VCC 
#          pin11(BCM:GPIO17) --- 红外DO
#          GND OV (board:pin39) ---  红外GND
#内容: 运行程序，按红外遥控器按键，检查GPIO 5和13对应的状态
# (1：GPIO5 闪烁  2：GPIO5 暂停并高亮  3：GPIO5 停止并熄灭 )
# (4：GPIO13 闪烁  5：GPIO13 暂停并高亮  6：GPIO13 停止并熄灭 )
#(EQ: 退出程序)

from ast import While
from time import sleep
import lirc
import RPi.GPIO as GPIO
import threading 

class FLASH_GPIO5(threading.Thread):
    def __init__(self,pin):
        super().__init__()
        self.pin = pin
        self.running = False
        self.run_pause = False
    
    def dostart(self):
        GPIO.setup(self.pin, GPIO.OUT)   
        GPIO.output(self.pin, GPIO.HIGH)
        self.pwm = GPIO.PWM(self.pin,50)
        self.pwm.start(50)

    def dostop(self):
        self.pwm.stop()
        GPIO.output(self.pin,GPIO.LOW)
        self.running = False

    def run(self):
        self.dostart()
        self.running = True
        while True:
            if not self.running:
                self.dostop()
                self.running = False
                return
            while self.run_pause:
                if not self.running:
                    self.dostop()
                    return
                else:
                    GPIO.output(self.pin,GPIO.HIGH)
                    pass
    def stop(self):
        self.running = False
    
    def pause(self):
        self.run_pause = True
    
    def resume(self):
        self.run_pause = False

class FLASH_GPIO13(threading.Thread):
    def __init__(self,pin):
        super().__init__()
        self.pin = pin
        self.running = False
        self.run_pause = False
    
    def dostart(self):
        GPIO.setup(self.pin, GPIO.OUT)   
        GPIO.output(self.pin, GPIO.HIGH)
        self.pwm = GPIO.PWM(self.pin,50)
        self.pwm.start(50)

    def dostop(self):
        self.pwm.stop()
        GPIO.output(self.pin,GPIO.LOW)
        self.running = False

    def run(self):
        self.dostart()
        self.running = True
        while True:
            if not self.running:
                self.dostop()
                self.running = False
                return
            while self.run_pause:
                if not self.running:
                    self.dostop()
                    return
                else:
                    GPIO.output(self.pin,GPIO.HIGH)
                    pass
    def stop(self):
        self.running = False
    
    def pause(self):
        self.run_pause = True
    
    def resume(self):
        self.run_pause = False



if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    Flash_5 = FLASH_GPIO5(5)
    Flash_5.setDaemon(True)
    flag_first_run_5 = True

    Flash_13 = FLASH_GPIO13(13)
    Flash_13.setDaemon(True)
    flag_first_run_13 = True

    sockid = lirc.init("myprogram", blocking=False)

    while True:
        try:
            code_ir = lirc.nextcode()
            if code_ir ==[u'1']:
                if Flash_5.running:
                    pass
                else:
                    print("GPIO5 LED START.")
                    if flag_first_run_5:                        
                        Flash_5.start()
                        flag_first_run_5 = False
                    else:
                        Flash_5 = FLASH_GPIO5(5)
                        Flash_5.setDaemon(True)
                        Flash_5.start()
            elif code_ir == [u'2']:
                if flag_first_run_5:
                    pass
                else:
                    if Flash_5.run_pause:
                        print("Resume GPIO5 LED")
                        Flash_5.resume()
                    else:
                        print("Pause GPIO5 LED")
                        Flash_5.pause()
            elif code_ir == [u'3']:
                if not Flash_5.running:
                    pass
                else:
                    print("Stop GPIO5 LED")
                    Flash_5.dostop()
            elif code_ir ==[u'4']:
                if Flash_13.running:
                    pass
                else:
                    print("GPIO13 LED START.")
                    if flag_first_run_13:                        
                        Flash_13.start()
                        flag_first_run_13 = False
                    else:
                        Flash_13 = FLASH_GPIO5(13)
                        Flash_13.setDaemon(True)
                        Flash_13.start()
            elif code_ir == [u'5']:
                if flag_first_run_5:
                    pass
                else:
                    if Flash_13.run_pause:
                        print("Resume GPIO13 LED")
                        Flash_13.resume()
                    else:
                        print("Pause GPIO13 LED")
                        Flash_13.pause()
            elif code_ir == [u'6']:
                if not Flash_13.running:
                    pass
                else:
                    print("Stop GPIO13 LED")
                    Flash_13.dostop()
            elif code_ir == [u'"EQ"']:
                print("User Quit.")
                break
        except KeyboardInterrupt:
            print("User Quit.")
            break
lirc.deinit()
GPIO.cleanup() 