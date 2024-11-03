# FileOutput 
from picamera2.outputs import FileOutput
output = FileOutput('test.h264')

#A memory buffer:
from picamera2.outputs import FileOutput
import io
buffer = io.Bytes()
output = FileOutput(buffer)

#A UDP network socket:
from picamera2.outputs import FileOutput
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(("REMOTEIP", 10001))
    stream = sock.makefile("wb")
    output = FileOutput(stream)