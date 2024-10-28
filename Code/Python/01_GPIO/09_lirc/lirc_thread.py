#硬件：RaspiberryPi 4B  + 红外接收模块
#连接方式： pin1(3_3V) --- 红外 VCC 
#          pin11(BCM:GPIO17) --- 红外DO
#          GND OV (board:pin39) ---  红外GND
#内容: 运行程序，按红外遥控器按键，检查GPIO5对应的状态（1：HIGH, 2:LOW,0:FLASH 10s,EQ:QUIT）

from time import sleep
import lirc
import RPi.GPIO as GPIO
import threading 


def GPIO_Setup(Pin,code_ir):
    """设置对应GPIO输出模式并且输出为1"""
    if code_ir == [u'1']:
        print(f"You press the button: {code_ir[0]}.")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pin,GPIO.OUT)
        GPIO.output(Pin,GPIO.HIGH)
    elif code_ir == [u'2']:
        print(f"You press the button: {code_ir[0]}.")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pin,GPIO.OUT)
        GPIO.output(Pin,GPIO.LOW)

def wait_time(Pin,code_ir,thired_stop):
    """延时"""
    if code_ir == [u'0']:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pin,GPIO.OUT)
        print(f"You press the button: {code_ir[0]}.")
        for i in range(10):
            if thired_stop.is_set():
                thired_stop.set()
                break
            GPIO.output(Pin,GPIO.LOW)
            sleep(1)
            GPIO.output(Pin,GPIO.HIGH)
            print(i)
            sleep(1)

sockid = lirc.init("myprogram", blocking=False)
thired_stop = threading.Event()
while True:
    try:
        code_ir = lirc.nextcode()
        if  code_ir:
            if code_ir == ['"EQ"']:
                thired_stop.set()
                print("thired stop.")
                break
            thread_1 = threading.Thread(target=wait_time,args=[5,code_ir,thired_stop])
            thread_2 = threading.Thread(target=GPIO_Setup,args=[5,code_ir])
            thread_1.start()
            thread_2.start()

    except KeyboardInterrupt:
        thread_1.join()
        thread_2.join()
        break

lirc.deinit()
GPIO.cleanup()