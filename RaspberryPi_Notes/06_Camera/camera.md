# 摄像头软件
- 官方摄像头
  - OV5647 (V1)
  - IMX219 (V2)
  - IMX477 (HQ)
  - IMX296 (GS)
  - IMX708 (V3)
- 第三方传感器
  - IMX290
  - IMX327
  - IMX378
  - OV9281
  - ...
# 软件库
- libcamera
  - libcamera-hello
    ```
    libcamera-hello --version
    libcamera-hello --help
    libcamera-hello
    libcamera-hello --qt preview
    libcamera-hello --timeout 10000 -o image.jpg
    ```
-rpicam
  - rpicam-hello
    ```
    rapicam-hello 短暂显示预览窗口5s
    rapicam-hello --timeout 0 无限运行，键盘中断
    rpicam-hello --info-text "red gain %rg, blue gain %bg" 显示当前的红色和蓝色增益值
    ```
    - 如果运行 X 窗口服务器并希望使用 X 转发，请使用 qt-preview 标志在 Qt窗口中呈现预览窗口。Qt 预览窗口比其他预览窗口占用更多资源
  - rpicam-jpeg
    - 捕获全分辨率的 JPEG 图像并将其保存↓
      - rpicam-jpeg --output /home/abc/Desktop/images/test.jpg
    - 命令显示预览窗口 2 秒钟，然后捕捉并保存分辨率为 640×480 像素的图像
      - rpicam-jpeg --output /home/abc/Desktop/images/test.jpg --timeout 2000 --width 640 --height 480
  - rpicam-still
    - 与 rpicam-jpeg 不同，rpicam-still 支持传统的 raspistill 应用程序中提供的许多选项。
      - rpicam-still --output /home/abc/Desktop/images/test.jpg
    - rpicam-still 可以保存多种格式的图像，包括png、bmp以及 RGB 和 YUV 二进制像素转储。要读取这些二进制转储，任何读取文件的应用程序都必须理解像素排列。
      - rpicam-still --encoding png --output /home/abc/Desktop/images/test.png
    - rpicam-still 可以捕获原始图像保存为test_o.dng文件
      -rpicam-still --raw --output /home/abc/Desktop/images/test_o.jpg
    - rpicam-still 捕捉长时间曝光
      - rpicam-still -o long_exposure.jpg --shutter 100000000 --gain 1 --awbgains 1,1 --immediate
    - rpicam-vid 捕获视频
      - rpicam-vid -t 10s -o /home/abc/Desktop/images/test.h264
      - vlc /home/abc/Desktop/images/test.h264 播放视频
      
      - 