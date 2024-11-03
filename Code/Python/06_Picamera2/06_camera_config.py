from time import sleep
from picamera2 import Picamera2
from libcamera import Transform,ColorSpace
picam2 = Picamera2()

# transform:     画面翻转 Transform(hflip=1,vflip=1)
# colour_space:  颜色空间 ColorSpace.Sycc()/SMPTE170M()/Rec709()
#               【preview和still的默认为Sycc】
#               【Video如果主流请求 RGB 格式则选择 Sycc。对于 YUV 格式如果分辨率小于 1280x720，它将选择 SMPTE 170M，否则选择 Rec.709】
# buffer_count:  为相机系统分配了多少组缓冲区（每个请求的流一组）以供使用。分配更多缓冲区可能意味着相机运行更流畅，
#               丢帧更少，但缺点是，尤其是在高分辨率下，可能没有足够的可用内存。
#               建议：preview：4， still：1， video: 6
# queue:        默认情况下保留从相机接收的最后一帧，当您发出捕获请求时，该帧可能会返回给您。
#               这对于突发捕获非常有用，特别是当应用程序正在执行一些可能需要比帧周期稍长的处理时。禁止:queue=False
#               注：当buffer_count=1时 不会有帧排队。
# display:      显示流 preview: main,  still: None(不会将任何图像渲染到预览窗口)
# encode:       视频录制开始时将被编码的流（main或lores） preview: main,  still: None
#               以下config允许录制 QVGA 流，同时允许同时捕获 2048x1536 静止图像
#               (main={"size": (2048, 1536)}, lores={"size": (320,240)}, encode="lores"
# lores:        三个流均可使用 size format 例：{"size":(800,600),"fromat":"RGB888"}
# size & format {"size":(800,600)} {"format":"RGB888"}
#               picam2.align_configuration(config)请求最佳
#               format：XBGR8888[R,G,B,255], XRGB8888[B,G,R,255], RGB888[B,G,R], BGR888[R,G,B], YUV420
#               OPENCV:RGB888
config = picam2.create_preview_configuration(transform=Transform(hflip=1),colour_space=ColorSpace.Sycc(),buffer_count=4,
                                             queue=False,lores={"size":[320,240]},display="lores",)
still_config = picam2.align_configuration()
picam2.configure(config)
picam2.start(show_preview=True)

sleep(5)