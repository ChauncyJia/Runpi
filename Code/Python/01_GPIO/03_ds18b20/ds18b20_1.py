#硬件：RaspiberryPi 4B  + DS18B20
#连接方式： pin2(5V) --- DS18B20 VCC 
#          pin7(BCM:GPIO4) --- DS18B20 D0
#          GND OV (board:pin6) ---  DS18B20 GND
#内容: 运行程序，每隔5s读取温度并打印出来，CTRL+C 退出
import os
import time

class Ds18b20():
    """DS18B20温度的类"""
    def __init__(self,str_id):
        """初始化str_id"""
        self.str_id = str_id

    def read_temp(self):
        """读取并返回温度值
        如果失败,返回False.
        """
        location = os.path.join(f"/sys/bus/w1/devices/{self.str_id}/w1_slave")
        if os.path.exists(location):
            with open(location) as f:
                lines = f.read().splitlines()
                text = lines[-1]
                temperaturedate = text.split(" ")[-1]
                temperaturedate = float(temperaturedate[2:])
                return temperaturedate/1000.0
        else:
            return False


if __name__ == "__main__":

    while True:
        try: 
            str_id = "28-0215033ef5ff"
            temp = Ds18b20(str_id)
            temp_value = temp.read_temp()
            print(f"温度:{temp_value}\n")
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nUser quit.")
            break

        