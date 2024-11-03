# 能够要求 Picamera2 捕获图像但在此过程中不要阻塞您的线程
# capture 和 switch_mode_and_capture 带有两个参数 
# wait 
# signal_function 
# 如果 wait 和 signal_function 均为 None，则函数将阻塞，直到操作完成。这就是我们可能称之为 “通常” 行为。
# 如果 wait 为 None 但提供了 signal_function，则该函数不会阻塞，而是立即返回，即使操作未完成。调用者应使用提供的 signal_function 在操作完成时通知应用程序。
# 如果提供了 signal_function，并且 wait 不是 None，则 wait 的给定值决定该函数是否阻塞（如果 wait 为 true，则阻塞）。然而，signal_function 仍然被调用。
# 您还可以将 wait 设置为 False，而不提供 signal_function。在这种情况下，函数会立即返回，您可以稍后阻止以完成操作（请参阅下文）。
from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
still_config = picam2.create_still_configuration()
picam2.configure(picam2.create_preview_configuration())
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(3)

job = picam2.switch_mode_and_capture_file(still_config,"24.jpg",wait=False)

for i in range(20):
    time.sleep(0.1)
    print(i)

metadate = picam2.wait(job)
