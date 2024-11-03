#CircularOutput 类派生自 FileOutput，并添加了使用几秒钟前的视频帧开始录制的功能。这是运动检测和安全应用的理想选择。
# CircularOutput 构造函数接受以下可选参数：

#file           （默认为 None） - 一个字符串 （表示文件名） 或用于构造 FileOutput 的类文件对象。这是写入循环缓冲区输出的位置。
#               值 None 表示，在创建循环缓冲区时，它将在循环缓冲区中累积帧，但不会将它们写出到任何位置。

#bufferSize   （默认为 150）- 将此项设置为您希望在当前时间之前能够访问的视频秒数乘以帧速率。
#               因此，150 个缓冲区足以以 30fps 的速度播放 5 秒的视频。

from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput
from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration())

encoder = H264Encoder()
output = CircularOutput()

picam2.start_recording(encoder, output)
output.fileoutput = "file.h264"
output.start()
time.sleep(5)
# Now when it's time to start recording the output, including the previous 5 seconds:
# And later it can be stopped with:
output.stop()
