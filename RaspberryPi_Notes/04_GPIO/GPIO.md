- 基本知识
  - pinout 输出各个pin定义BCM编码
  - 安装waringPi 后指令：gpio readall 可读取各端口状态
- BCM码利用wiringPi的GPIO 指令控制灯亮灭
```
 gpio -g mode 4 out
 gpio -g read 4
 gpio -g write 4 1
 gpio -g write 4 0
```
- 控制硬件指令
  - 516对应的BCM的pin，以为本Rasp 4B 0 为512
```
cd /sys/class/gpio
ls
echo 516 > export
cd gpio516
echo out > direction
echo 1 > value
echo 0 > value
cd ..
echo 516 > unexport
ls
```