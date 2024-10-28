import RPi.GPIO as GPIO
import time

# DHT11 Sensor Pin
DHT11_PIN = 26  # GPIO26对应的BCM编号，根据您的实际情况可能需要调整

# 设置GPIO的编号模式
GPIO.setmode(GPIO.BCM)
# 设置GPIO引脚为输入模式
GPIO.setup(DHT11_PIN, GPIO.OUT)

# DHT11 数据位数量
DHT11_DATA = 40

def read_dht11_data(pin):
    # 设置数据引脚为高电平，持续至少18ms
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.025)
    # 设置数据引脚为输入模式
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # 等待传感器响应
    while GPIO.input(pin) == GPIO.HIGH:
        continue
    while GPIO.input(pin) == GPIO.LOW:
        continue

    # 读取数据
    data = [0] * DHT11_DATA
    for i in range(DHT11_DATA):
        while GPIO.input(pin) == GPIO.LOW:
            continue
        pulse_start_time = time.time()
        while GPIO.input(pin) == GPIO.HIGH:
            continue
        pulse_duration = (time.time() - pulse_start_time) * 1000000  # us

        if i % 2 == 0:
            data[i] = int(pulse_duration / 1000) & 0x01
        else:
            data[i] = pulse_duration / 1000

    # 计算校验和
    if (data[0] + data[1] + data[2] + data[3]) & 0xFF == data[4]:
        return data[2], data[0] + (data[1] << 8), data[3]
    else:
        return None

try:
    while True:
        data = read_dht11_data(DHT11_PIN)
        if data is not None:
            humidity, temperature, _ = data
            print("湿度: {:.1f}%".format(humidity))
            print("温度: {:.1f}°C".format(temperature))
        else:
            print("读取DHT11数据失败")
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()