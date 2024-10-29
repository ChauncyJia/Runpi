#硬件：RaspiberryPi 4B  + SG90舵机
#连接方式： pin2(5V) --- G90舵机 红色VCC 
#          pin33(BCM:GPIO13) --- G90舵机 黄色DO
#          GND OV (board:pin39) ---  棕色GND
#内容: 运行程序，舵机持续运作180°
# GPIO 12、GPIO 13、GPIO 18和GPIO 19 是硬件PWM


import RPi.GPIO as GPIO
import time


def set_servo_angle(angle):
    # 将角度转换为对应的占空比
    global min_duty_cycle
    global max_duty_cycle
    duty_cycle = (angle / 180.0) * (max_duty_cycle - min_duty_cycle) + min_duty_cycle
    print(duty_cycle)
    duty_cycle = max(min_duty_cycle, min(duty_cycle, max_duty_cycle))  # 限制占空比在有效范围内
    print(duty_cycle)
    pwm.ChangeDutyCycle(duty_cycle)

GPIO.setmode(GPIO.BCM)
pwm_pin = 13


# 设置舵机的最小和最大角度对应的占空比（这些值可能需要根据实际情况调整）
min_duty_cycle = 2.5  # 对应大约0度
max_duty_cycle = 12.5 # 对应大约180度

# 初始化GPIO通道为PWM输出
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 50)
pwm.start(0)  # 初始占空比为0
while True:
    try:
        # 循环测试舵机从0度到180度
        for angle in range(0, 181):
            set_servo_angle(angle)
            time.sleep(0.02)  # 稍微等待一下，以便观察舵机的动作
        for angle in range(180, -1, -1):
            set_servo_angle(angle)
            time.sleep(0.02)  # 稍微等待一下，以便观察舵机的动作
    except KeyboardInterrupt:
        break
    
pwm.stop()
GPIO.cleanup()