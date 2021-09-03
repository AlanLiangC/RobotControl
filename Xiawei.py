import serial
import time
from Over2 import get_whole
from Circle2 import get_circle
# 串口打开函数
def open_ser():
    port = 'COM3'  # 串口号
    baudrate = 115200  # 波特率
    try:
        global ser
        ser = serial.Serial(port, baudrate, timeout=2)
        if (ser.isOpen() == True):
            print("串口打开成功")
    except Exception as exc:
        print("串口打开异常", exc)

# 数据发送
def send_msg(some):
    try:
        send_datas1 = some
        ser.write(str(send_datas1).encode("gbk"))
        print("已发送数据:", send_datas1)
    except Exception as exc:
        print("发送异常", exc)

# 接收数据
def read_msg():
    try:
        #print("等待接收数据")
        while True:
            data = ser.read(ser.in_waiting).decode('gbk')
            if data != '':
                break
        print("已接受到数据:", data)
    except Exception as exc:
        print("读取异常", exc)

# 关闭串口
def close_ser():
    try:
        ser.close()
        if ser.isOpen():
            print("串口未关闭")
        else:
            print("串口已关闭")
    except Exception as exc:
        print("串口关闭异常", exc)


def draw_Line(x0,y0,xe,ye):
    open_ser()  # 打开串口
    send_msg("L"+"\r\n")  # 写数据
    time.sleep(0.5)
    read_msg()  # 读数据
    liang =  get_whole(x0,y0,xe,ye)
    for i in liang:
        i = int(i)
        send_msg(str(i) + "\r\n")  # 写数据
        #time.sleep(0.001)
        #read_msg()  # 读数据
    send_msg("O" + "\r\n")  # 写数据
    read_msg()  # 读数据
    read_msg()  # 读数据
    #time.sleep(3)
    #read_msg()  # 读数据
    close_ser()  # 关闭串口

def draw_circle(x0,y0,xe,ye,r,sn):
    #x0,y0,xe,ye = eval(input("请输入圆弧段的起始点："))
    #r,sn = eval(input("请输入圆弧的半径（0：逆圆；1：顺圆）："))
    open_ser()  # 打开串口
    send_msg("L" + "\r\n")  # 写数据
    time.sleep(0.5)
    read_msg()  # 读数据
    liang =  get_circle(x0,y0,xe,ye,r,sn)
    print(liang)
    for i in liang:
        i = int(i)
        send_msg(str(i) + "\r\n")  # 写数据
        #time.sleep(0.001)
        #read_msg()  # 读数据
    send_msg("O" + "\r\n")  # 写数据
    read_msg()  # 读数据
    read_msg()  # 读数据
    close_ser()  # 关闭串口





#draw_circle(0,100,100,0,100,1)
#draw_Line(0,100,100,0)



