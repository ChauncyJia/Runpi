#硬件：RaspiberryPi 4B  + DHT11 温湿度
#连接方式： pin1(3_3V) --- DHT11 VCC 
#          pin37(BCM:GPIO26) --- DHT11 DATA
#          GND OV (board:pin39) ---  DS18B20 GND
#内容: 运行程序，每隔5s读取温湿度并打印出来，CTRL+C 退出

import RPi.GPIO as GPIO
import time

class DHT11():
    
    def __init__(self,pin_dht):
        self.pin = pin_dht

    def collect_input(self):
        """收集线上传来的数据"""
        #记录持续信号时长
        unchanged_count = 0
        #信号持续的最大长度
        max_unchanged_count = 100
        last = -1
        data = []
        while True:
            #不断采集数据
            current = GPIO.input(self.pin)
            data.append(current)
            #记录信号持续的时间
            #如果有变化就开始一段新的记录
            if last != current:
                unchanged_count = 0
                last = current
            #没有变化的次数＋1
            else:
                unchanged_count += 1
                if unchanged_count > max_unchanged_count:
                    break
        return data

    def get_high_state_lengths_data(self,data):
        """从收集的信号中获取数据位高电平的的持续时间"""
        #设置5个状态 分别为 初始延时 起始位低电平，起始位高电平，数据位低电平，数据位高电平
        STATE_DELAY_H = 1
        STATE_START_L = 2
        STATE_START_H = 3
        STATE_DATA_L = 4
        STATE_DATA_H = 5
        state = STATE_DELAY_H

        lengths = [] #记录每个数据周期中的高电平持时间
        current_length = 0 #记录前一个状态的持续时间

        for i in range(len(data)):
            current = data[i]
            current_length += 1

            #等待的高电平
            if state == STATE_DELAY_H:
                if current == GPIO.LOW:
                    state = STATE_START_L
                    continue
                else:
                    continue
            #起始的低电平
            if state == STATE_START_L:
                if current == GPIO.HIGH:
                    state = STATE_START_H
                    continue
                else:
                    continue
            #起始的高电平
            if state == STATE_START_H:
                if current == GPIO.LOW:
                    state = STATE_DATA_L
                    continue
                else:
                    continue
            #数据的低电平
            if state == STATE_DATA_L:
                if current == GPIO.HIGH:
                    current_length = 0
                    state = STATE_DATA_H
                    continue
                else:
                    continue
            #数据的高电平
            if state == STATE_DATA_H:
                if current == GPIO.LOW:
                    lengths.append(current_length)
                    state= STATE_DATA_L
                    continue
                else:
                    continue

        return lengths

    def calculate_bits(self,high_state_lengths_data):
        """记录数据高电平时长进行0/1解码"""
        #找到最长和最短的时长
        shortest_pull_up = 1000
        longest_pull_up = 0
        
        for i in range(0, len(high_state_lengths_data)):
            length = high_state_lengths_data[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length
        #用中间值作为阈值
        halfway = (longest_pull_up + shortest_pull_up) / 2
        bits = []
        #大于阈值判定为1，否则判定为0
        for i in range(0, len(high_state_lengths_data)):
            bit = False
            if high_state_lengths_data[i] > halfway:
                bit = True
                bits.append(bit)
        return bits
    
    def bits_to_bytes(self,bits):
        """每8个bit一组 将bit变为byte"""
        the_bytes= []
        byte = 0
        for i in range(0,len(bits)):
            byte = byte << 1
            if (bits[i]):
                byte = byte | 1
            else:
                byte = byte | 0
            if((i + 1) % 8 == 0):
                the_bytes.append(byte)
                byte = 0
        return the_bytes
    
    def calculate_checksum(self, the_bytes):
        """计算校验值 前四个字节相加取低8位作为校验码"""
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255


    def read_DHT(self):
        #设置为输出引脚
        GPIO.setup(self.pin,GPIO.OUT)
        #输出高电平
        GPIO.output(self.pin,GPIO.HIGH)
        time.sleep(0.05)
        #输出低电平
        GPIO.output(self.pin,GPIO.LOW)
        time.sleep(0.02)

        #放弃总线控制权
        GPIO.setup(self.pin,GPIO.IN,GPIO.PUD_UP)

        #收集从数据线上传来的数据
        data = self.collect_input()

        #从收集的信号中获取数据位，高电平持续时间
        high_state_lengths_data = self.get_high_state_lengths_data(data)

        #数据应当有40位，有40段高电平，包括4字节数据和1字节校验不对的话退出
        if len(high_state_lengths_data) != 40:
            return False,0
        
        #根据上升脉冲的长度计算二进制bit
        bits = self.calculate_bits(high_state_lengths_data)

        #将二进制bit变换为字节
        the_bytes = self.bits_to_bytes(bits)

        #进行校验，校验失败返回错误信息
        checksum = self.calculate_checksum(the_bytes)

        if the_bytes[4] != checksum:
            return False,0
        
        #四个字节0-3 分别是湿度的整数，湿度的小数，温度的整数，温度的小数
        temperature = the_bytes[2] + float(the_bytes[3]) / 10
        humidity = the_bytes[0] + float(the_bytes[1]) / 10

        #正确接收返回接收正确标志位的数据
        return True, [temperature, humidity]


if __name__ == "__main__":

    pin_dht = 26
    GPIO.setmode(GPIO.BCM)

    Temp_dht = DHT11(pin_dht)

    while True:
        try:
            flag, result = Temp_dht.read_DHT()
            if flag:
                print(f"温度：{result[0]}")
                print(f"湿度：{result[1]}")
            else:
                print("DHT11_ERROR!!!")
            time.sleep(5)
        except KeyboardInterrupt:
            print("USER Quit.")
            break

    GPIO.cleanup()
