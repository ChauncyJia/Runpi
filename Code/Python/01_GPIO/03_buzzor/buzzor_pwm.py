#硬件：RaspiberryPi 4B  无源蜂鸣器(低电平触发)
#连接方式：3_3V pin1 --- 连接蜂鸣器 VCC
#         BCM17 (board:pin11) ---  连接蜂鸣器I/O
#         GND OV (board:pin25) ---  连接蜂鸣器GND
#内容: 运行程序，蜂鸣器播放音乐； CTRL+C 退出。

import RPi.GPIO as GPIO   #导入RPi的GPIO
from time import sleep

class BuzzorSong():
    """创建一个蜂鸣器歌曲的类"""
    def __init__(self,pin_buzzor,delay_beat):
        """初始化属性,设置pwm模式"""
        self.pin_buzzor = pin_buzzor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_buzzor,GPIO.OUT)
        GPIO.output(pin_buzzor,GPIO.HIGH)
        self.buzzor_pwm = GPIO.PWM(pin_buzzor, 1440) #频率
        self.buzzor_pwm.start(50) #占空比
        self.dealy_beat = delay_beat

        self.note2freq = {"cl1":131,"cl2":147,"cl3":165,"cl4":175,"cl5":196,"cl6":211,"cl7":248,
                          "cm1":262,"cm2":294,"cm3":330,"cm4":250,"cm5":393,"cm6":441,"cm7":495,
                          "ch1":525,"ch2":589,"ch3":661,"ch4":700,"ch5":786,"ch6":882,"ch7":990,
                          }
        
    def play_song(self,notes,beats):
        """播放曲目"""
        for note,beat in zip(notes,beats):
            self.buzzor_pwm.ChangeFrequency(self.note2freq[note])
            sleep(self.dealy_beat*beat)
    
    def stop_song(self):
        """停止播放曲目"""
        self.buzzor_pwm.stop()
        GPIO.output(self.pin_buzzor,GPIO.HIGH)

if __name__ == "__main__":

    pin_buzzor = 17
    buzzor_song = BuzzorSong(pin_buzzor,delay_beat=0.3)

    #音符
    notes = ['cm1', 'cm1', 'cm1', 'cl5', 'cm3', 'cm3', 'cm3', 'cm1',
             'cm1', 'cm3', 'cm5', 'cm5', 'cm4', 'cm3', 'cm2', 'cm2',
             'cm3', 'cm4', 'cm4', 'cm3', 'cm2', 'cm3', 'cm1', 'cm1',
             'cm3', 'cm2', 'cl5', 'cl7', 'cm2', 'cm1']
    #节拍
    beats = [1, 1, 2, 2, 1, 1, 2, 2,
             1, 1, 2, 2, 1, 1, 3, 1,
             1, 2, 2, 1, 1, 2, 2, 1,
             1, 2, 2, 1, 1, 3]
    
    while True:
        try:
            buzzor_song.play_song(notes,beats)
            buzzor_song.stop_song()
            print("Finished")
        except KeyboardInterrupt:
            print("User Quit.")
            break
    GPIO.cleanup()    