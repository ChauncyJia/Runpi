- BCM码利用wiringPi的GPIO 指令控制灯亮灭
```
 gpio -g mode 4 out
 gpio -g read 4
 gpio -g write 4 1
 gpio -g write 4 0
```


- 控制硬件指令
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