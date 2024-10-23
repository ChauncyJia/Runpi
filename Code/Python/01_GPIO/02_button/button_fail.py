#硬件：RaspiberryPi 4B  OV5647树莓派v1摄像头
#连接方式：GPIO17 (board:pin11) ---  连接up开关一端
#          GPIO27 (board:pin13) ---  连接Left开关一端
#          GPIO22 (board:pin15) ---  连接right开关一端
#         GND OV (board:pin39) ---  连接up,left,rigt开关另一端
#内容: 运行程序，按up按钮 摄像机拍照并保存桌面 
#按left按钮，相机启动预览，按right按键关闭预览 键盘中断
# ```
# from time import sleep
# from gpiozero import Button
# from picamera2 import Picamera2
# from datetime import datetime
# from signal import pause

# button_up = Button(17)
# button_left = Button(27)
# button_right = Button(22)
# camera = Picamera2()


# def capture():
#     #camera.capture_file(f'/home/abc/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')
#     file_path =f"/home/abc/Desktop/{datetime.now():%Y-%m-%d-%H-%M-%S}"
#     camera.start_and_capture_file(f'{file_path}.jpg')
#     camera.stop_preview()

# while True:
#     try:
#         if button_up.value  == 1:
#             capture()
#         if button_left.value == 1:
#             camera.start_preview()
#         if button_right.value == 1:
#             camera.stop_preview()

#     except KeyboardInterrupt:
#          print("User Quit")
#          break
# #pause()
# ````