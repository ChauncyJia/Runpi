import serial
from time import sleep

#serial setup
ser = serial.Serial("/dev/serial0",9600,8,'N',1,1)

#serial check
if not ser.isOpen():
    print("Open Serial Failed.")
else:
    print("Open Serial Succeess.")
    print(ser)

def autoreply():
    try:
        while True:
            #Read data from PC com
            data = ser.read(ser.inWaiting())
            if data:
                #print data
                print("Recv:",data.decode("utf-8"))
                #return data to PC
                ser.write(data)
                print("Send:",data.decode("utf-8"))
            # delay
            sleep(0.05)   
    except KeyboardInterrupt:
        print("User Quit!")
    except serial.SerialException as e:
        print("Serial error:",e)
        
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
        print("User Quit!")
    except serial.SerialException as e:
        print("Serial error:",e)
        
def onlyrecv():
    try:
        while True:
            #Read data from PC com
            data = ser.read(ser.inWaiting())
            if data:
                #print data
                print("Recv:",data.decode("utf-8"))
            # delay
            sleep(0.05)   
    except KeyboardInterrupt:
        print("User Quit!")
    except serial.SerialException as e:
        print("Serial error:",e)

#this is Main
while True:
    print("Hello, This is Serial test program.Please input 'auto/manual/recv'to enter Mode. Enter'q' is quit.\r")
    inway = input("Mode:")
    print(inway)
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
ser.close()
    