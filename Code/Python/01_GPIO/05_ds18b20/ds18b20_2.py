#硬件：RaspiberryPi 4B  + DS18B20
#软件：需安装python的w1thermsensor库
#连接方式： pin2(5V) --- DS18B20 VCC 
#          pin7(BCM:GPIO4) --- DS18B20 D0
#          GND OV (board:pin6) ---  DS18B20 GND
#内容: 运行程序，每隔5s读取温度并打印出来，CTRL+C 退出

import glob
import time
from w1thermsensor import W1ThermSensor as w1

str_id = "28-0215033ef5ff"
sensor_path = glob.glob(f"sys/bus/w1/devices/{str_id}")
print(sensor_path)
sensor = w1(sensor_path)

while True:
    try:
        temperaure = sensor.get_temperature()
        print(f"Current temperature: {temperaure}℃")
        time.sleep(5)

    except KeyboardInterrupt:
        print("User Quit.")
        break