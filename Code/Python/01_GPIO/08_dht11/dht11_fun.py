import time
import board
import adafruit_dht

# 选择DHT传感器类型和GPIO引脚
sensor = adafruit_dht.DHT11(board.D26)  

while True:
    try:
        # 读取湿度和温度
        humidity = sensor.humidity
        temperature = sensor.temperature

        # 打印湿度和温度
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))

    except RuntimeError as error:
        # 错误处理，DHT传感器读取可能不总是成功的
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        print("An unexpected error occurred: {}".format(error))
        break

    # 每3秒读取一次数据
    time.sleep(3)
