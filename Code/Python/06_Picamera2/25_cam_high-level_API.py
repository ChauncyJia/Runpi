#高级API
from picamera2 import Picamera2

picam2 = Picamera2


picam2.start_and_capture_file("25.jpg")  #捕获单张图片
#name               保存捕获图像的文件名。
#dealy              捕获图像之前的延迟秒数。值 0 （no delay） 有效。
#preview_mode       用于操作预览阶段的相机配置。默认值指示使用 Picamera2 对象的 Preview_configuration 字段中的配置，
#                   但可以提供任何其他配置。如果延迟大于零，则捕获操作仅具有预览阶段。
#capture_mode       用于捕获图像的相机配置。默认值指示使用 Picamera2 对象的 still_configuration 字段中的配置，但可以提供任何其他配置。
#show_preview       预览
#exit_data

picam2.start_and_capture_files("test{:d}.jpg", initial_delay=5, delay=5, num_files=10)  #捕获多图片

# initial_delay 捕获第一张照片前的延迟
# num_files     捕获图片数量
# dealy         除了首张，其他所有图片捕获之间的秒数，如果0则捕获之间不存在预览阶段