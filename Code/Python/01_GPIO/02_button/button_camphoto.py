#硬件：RaspiberryPi 4B  OV5647树莓派v1摄像头
#连接方式：BCM21 (board:pin40) ---  连接开关一端
#         GND OV (board:pin39) ---  连接开关另一端
#内容: 运行程序，按下按钮 摄像机拍照并保存到桌面保持预览界面 键盘中断

from time import sleep
from gpiozero import Button
from picamera2 import Picamera2
from datetime import datetime
from signal import pause

button = Button(21)
camera = Picamera2()


def capture():
    #camera.capture_file(f'/home/abc/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')
    file_path =f"/home/abc/Desktop/{datetime.now():%Y-%m-%d-%H-%M-%S}"
    camera.start_and_capture_file(f'{file_path}.jpg')
    #camera.capture_file(file_path)

button.when_activated = capture
sleep(8)
#pause()
