#捕获10s视频
from email.policy import default
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder,Quality,JpegEncoder,MJPEGEncoder
import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(bitrate=10000000)
output = "nihao.h264"

picam2.start_recording(encoder, output,quality=Quality.HIGH)
time.sleep(10)
picam2.stop_recording()

#多次启动和停止
""" picam2.start_encoder(encoder, output)
picam2.satrt() """

#录制中

""" picam2.stop()
picam2.stop_encoder() """

#recording 编码器质量选项quality=
# Quality.VERY_LOW
# Quality.LOW
# Quality.MEDIUM(default)
# Quality.HIGH
# Quality.VERY_HIGH

# 一半的速录进行编码
# encoder.frame_skip_count = 2

test_encoder = H264Encoder()
# H264Encoder设置
# bitrate    要使用的比特率（以每秒位数为单位）。默认值 None 将导致编码器在启动时根据 Quality 选择合适的比特率。
# repeat     是否对每个 Intra 帧（I 帧）重复流的序列标头。当通过网络流式传输视频时，当客户端可能无法接收序列标头通常所在的流的开头时，这有时非常有用
# iperiod    从一个 I 帧到下一个 I 帧的帧数。值 None 将此值留给硬件自行决定，默认为 60 帧。
#该编码器可以接受 3 通道 RGB（“RGB888”或“BGR888”）、4 通道 RGBA（“XBGR8888”或“XRGB8888”）或YUV420 （“YUV420”） 的定义。

test_encoder = JpegEncoder()
# JpegEncoder            设置 类实现多线程软件 JPEG 编码器，该编码器也可以用作运动 JPEG （“MJPEG”） 编码器
# nem_threads            并发线程数目
# q                      JPEG 品质编号 默认值 None 将导致编码器在启动时根据 Quality 选择适当的值。
# colour_space          软件将为正在编码的流选择正确的 “色彩空间”，因此此参数通常应留空。
# colour_subsampling    （默认为 420）- 这是编码器在编码之前将 RGB 像素在内部转换为 YUV 的形式。因此，它决定了 JPEG 解码器会看到 YUV420 图像还是其他图像。
#                       有效值为 444 （YUV444）、422 （YUV422）、440 （YUV440）、420（YUV420，默认值）、411 （YUV411） 或灰度（灰度）
# 该编码器可以接受三通道 RGB（“RGB888”或“BGR888”）或 4 通道 RGBA（“XBGR8888”或“XRGB8888”）。请注意，不能向其传递任何 YUV 格式。

test_encoder = MJPEGEncoder()
#MJPEGEncoder 类使用 Raspberry Pi 的内置硬件实现 MJPEG 编码器，可通过 V4L2 内核驱动程序访问。构造函数接受以下可选参数：
#• bitrate （default None） -要使用的比特率（以每秒位数为单位）。默认值 None 将导致编码器在启动时根据 Quality 选择合适的比特率。
# 该编码器可以接受 3 通道 RGB（“RGB888”或“BGR888”）、4 通道 RGBA（“XBGR8888”或“XRGB8888”）或 YUV420（“YUV420”）。