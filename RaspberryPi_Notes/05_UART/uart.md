- 树莓派串口分为主和辅UART:
```
mini uart   /dev/ttys0
hard uart  /dev/ttyAMA0    TX:8  RX:10
primary UART /dev/serial0  main
secondary UART /dev/serial1  sub
```
- 使用命令查看串口打开情况
  - ls /dev/serial* -l
  - 确保lrwxrwxrwx 1 root root 5 Oct 13 20:35 /dev/serial0 -> ttyS0
- 使用sudo raspi-config 进入interfa option 关闭串口启动，启用串口硬件

minicom :
sudo minicom -D /dev/serial0 -b 9600