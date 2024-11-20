import serial
import RPi.GPIO as GPIO
import time

# 设置GPIO引脚编号模式
GPIO.setmode(GPIO.BCM)

# 设置GPIO引脚为输出模式，这里以GPIO 17为例
GPIO.setup(17, GPIO.OUT)

# 设置串口参数
ser = serial.Serial(
    port='/dev/serial0',  # 串口设备文件，根据实际情况修改
    baudrate=115200,      # 波特率
    parity=serial.PARITY_NONE,  # 奇偶校验位
    stopbits=serial.STOPBITS_ONE,  # 停止位
    bytesize=serial.EIGHTBITS,  # 数据位
    timeout=1           # 读取超时时间
)

# 循环读取串口数据
while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print("Received:", line)
            
            # 根据接收到的命令控制GPIO引脚
            if line == 'ON':
                GPIO.output(17, GPIO.HIGH)  # 打开引脚17
                print("GPIO 17 is ON")
            elif line == 'OFF':
                GPIO.output(17, GPIO.LOW)  # 关闭引脚17
                print("GPIO 17 is OFF")
            elif line == 'TOGGLE':
                current_state = GPIO.input(17)
                GPIO.output(17, not current_state)  # 切换引脚17的状态
                print("Toggled GPIO 17")
            else:
                print("Unknown command")

        time.sleep(0.1)  # 简单的延时，减少CPU占用
    except KeyboardInterrupt:
        break

# 清理GPIO设置
GPIO.cleanup()