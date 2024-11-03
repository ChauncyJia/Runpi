#FfmpegOutput 类将编码的帧转发到 FFmpeg 进程。这为一些相当复杂的新类型输出打开了大门，包括 MP4 文件甚至音频，但可能需要大量的知识
from picamera2.outputs import FfmpegOutput

output = FfmpegOutput("test.mp4", audio=True)