#硬件：RaspiberryPi 4B  + 红外接收模块
#连接方式： pin1(3_3V) --- 红外 VCC 
#          pin11(BCM:GPIO17) --- 红外DO
#          GND OV (board:pin39) ---  红外GND
#内容: 运行程序，按红外遥控器12345按键，检查GPIO对应的状态

from time import sleep
import lirc
import RPi.GPIO as GPIO

def GPIO_Setup(Pin):
    """设置对应GPIO输出模式并且输出为1"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin,GPIO.OUT)
    GPIO.output(Pin,GPIO.HIGH)

sockid = lirc.init("myprogram", blocking=False)

while True:
    try:
        code_ir = lirc.nextcode()
        if code_ir == [u'1']:
            print(f"You press the button: {code_ir[0]}.")
            GPIO_Setup(5)
        elif code_ir == [u'2']:
            print(f"You press the button: {code_ir[0]}.")
            GPIO_Setup(6)
        elif code_ir == [u'3']:
            print(f"You press the button: {code_ir[0]}.")
            GPIO_Setup(13)
        elif code_ir == [u'4']:
            print(f"You press the button: {code_ir[0]}.")
            GPIO_Setup(19)
        elif code_ir == [u'5']:
            print(f"You press the button: {code_ir[0]}.")
            GPIO_Setup(26)
        elif code_ir == [u'"EQ"']:
            print('User Quit.')
            break

    except KeyboardInterrupt:
        break

lirc.deinit()
GPIO.cleanup()