import serial #导入serial
from time import sleep

#serial setup
ser = serial.Serial("/dev/serial0",115200,8,'N',1,1)

#serial check
if not ser.isOpen():
    print("Open Serial Failed.")
else:
    print("Open Serial Succeess.")
    print(ser)

#定义自动返回函数
def autoreply():
    try:
        while True:
            #Read data from PC com
            data = ser.read(ser.inWaiting())
            sleep(0.05)
            if data:
                #print data
                print("Recv:",data.decode("utf-8"))
                #return data to PC
                ser.write(data)
                print("Send:",data.decode("utf-8"))
            # delay
            sleep(0.05)   
    except KeyboardInterrupt:
        print("\nUser Quit!")
    except serial.SerialException as e:
        print("Serial error:",e)
#定义手动返回函数        
def manualreply():
    try:
        indata = str(input("Please intput data:"))
        indata = indata.encode("ascii")
        ser.write(indata)
        while True:
            #Read data from PC com
            data = ser.read(ser.inWaiting())
            if data:
                #print data
                print("Recv:",data.decode("utf-8"))
                #return data to PC
                indata = str(input("Please intput data:"))
                indata = indata.encode("ascii")
                ser.write(indata)
            # delay
            sleep(0.05)   
    except KeyboardInterrupt:
        print("\nUser Quit!")
    except serial.SerialException as e:
        print("Serial error:",e)
#定义仅接收函数   
def onlyrecv():
    try:
        while True:
            #Read data from PC com
            data = ser.read(ser.inWaiting())
            if data:
                #print data
                print("Recv:",data.decode("utf-8"))
            # delay
            sleep(0.005)   
    except KeyboardInterrupt:
        print("\nUser Quit!")
    except serial.SerialException as e:
        print("Serial error:",e)

#this is Main
while True:
    try:
        # 请输入此程序运行的模式
        print("Hello, This is Serial test program.Please input 'auto/manual/recv'to enter Mode. Enter'q' is quit.\r")
        inway = input("Mode:")
        if inway == "auto":
            print("auto replay mode is open.")
            autoreply()
        elif inway == "manual":
            print("manualreplay mode is open.")
            manualreply()
        elif inway == "recv":
            print("only recv mode is open.")
            onlyrecv()
        elif inway =="q":
            print("your are quit success..")
            break
        else:
            print("Your input is incorrect!")
    except KeyboardInterrupt: #键盘中断
        print("\nUser Quit!")
        break
#关闭serial       
ser.close()
    