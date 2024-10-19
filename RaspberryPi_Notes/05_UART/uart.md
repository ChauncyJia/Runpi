- 使用命令查看串口打开情况
  - ls /dev/serial* -l
  - 确保lrwxrwxrwx 1 root root 5 Oct 13 20:35 /dev/serial0 -> ttyS0
- 使用sudo raspi-config 进入interfa option 关闭串口启动，启用串口硬件
- 增加serial1 显示，并将serial0 设为ttyAMA0
  - sudo nano /boot/firmware/config.txt
  - 在文件中增加 dtparam=krnbt=off
  - dtoverlay=miniuart-bt [https://pidoc.cn/docs/computers/configuration#uart%E5%92%8C%E8%AE%BE%E5%A4%87%E6%A0%91]
  - force_turbo=1 
  - ls /dev -al 查看
- 展示所有uart
  - dtoverlay -a | grep uart
- 查看特定串口信息
  - dtoverlay -h uart2 相关信息：[https://blog.csdn.net/yhhdll0107/article/details/123327413]
- 树莓派串口分为主和辅UART:
```
mini uart   /dev/ttys0
hard uart  /dev/ttyAMA0    TX:8  RX:10
primary UART /dev/serial0  main
secondary UART /dev/serial1  sub
```
minicom :
sudo minicom -D /dev/serial0 -b 9600