import turtle
from tkinter import *
import tkinter as tk
import hashlib
import math
from Xiawei import *
import serial.tools.list_ports

sn = 0          #判断逆时针顺时针 0为逆时针 1为顺时针
way = 0
T = 0
beishu = 10
pointss = []
plist = list(serial.tools.list_ports.comports())
shi = {"S":0,"N":0,"G":0,"D":0}
Theta0 = 0
point = (0,0)
number = 2

if len(plist) <= 0:
    print("The Serial port can't find!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]

root = tk.Tk()
root.title('数控插补演示界面')
root.geometry('850x600')
canvas = tk.Canvas(master=root, bd=5, width =400, height =400)    #创建画布
canvas.place(x = 200,y = 10)
turtle = turtle.RawTurtle(canvas)
turtle.hideturtle()
color_1 = (0, 191, 255)
color_2 = (255, 181, 197)

bianc = tk.Label(root, text="编程窗口")  # 标签
bianc.place(x = 630,y = 10)
biancheng = tk.Text(root, width=30, height=28, undo=True, autoseparators=False)
biancheng.place(x = 630,y = 30)


chuan = tk.Label(root, text="端   口")  # 标签
chuan.place(x = 20,y = 20)

bote = tk.Label(root, text="波特率")  # 标签
bote.place(x = 20,y = 50)

zhixian = tk.Label(root, text="直   线")  # 标签
zhixian.place(x = 20,y = 80)

zzuobiao = tk.Label(root, text="直线坐标")  # 标签
zzuobiao.place(x = 20,y = 110)

yuanhu = tk.Label(root, text="圆   弧")  # 标签
yuanhu.place(x = 20,y = 140)

yxzuobiao = tk.Label(root, text="圆弧半径")  # 标签
yxzuobiao.place(x = 20,y = 170)

yzuobiao = tk.Label(root, text="起点坐标")  # 标签
yzuobiao.place(x = 20,y = 200)

shij = tk.Label(root, text="示校模式")  # 标签
shij.place(x = 20,y = 430)
v5 = tk.IntVar()            # 用来表示按钮是否选中
v6 = tk.IntVar()
c5 = tk.Checkbutton(root, text='快进', variable=v5).place(x = 70,y = 428)
c6 = tk.Checkbutton(root, text='工进', variable=v6).place(x = 120,y = 428)

chushi = tk.Label(root, text="起点位置")  # 标签
chushi.place(x = 20,y = 460)

X = tk.Label(root, text="X")  # 标签
X.place(x = 25,y = 490)
X1 = tk.StringVar()
X1 = tk.Entry(root, textvariable=X1,width=5)  # 创建文本框
X1.place(x=45,y=490)

Y = tk.Label(root, text="Y")  # 标签
Y.place(x = 25,y = 520)
Y1 = tk.StringVar()
Y1 = tk.Entry(root, textvariable=Y1,width=5)  # 创建文本框
Y1.place(x=45,y=520)

L = tk.Label(root, text="L")  # 标签
L.place(x = 95,y = 490)
L1 = tk.Text(root,width=7, height=1, undo=True, autoseparators=False)
L1.place(x = 110,y = 490)

T = tk.Label(root, text="T")  # 标签
T.place(x = 95,y = 520)
T1 = tk.Text(root,width=7, height=1, undo=True, autoseparators=False)
T1.place(x = 110,y = 520)

D = tk.Label(root, text="当前点位置")  # 标签
D.place(x = 330,y = 460)
X2 = tk.Label(root, text="X")  # 标签
X2.place(x = 265,y = 490)
X22 = tk.Text(root,width=9, height=1, undo=True, autoseparators=False)
X22.place(x = 280,y = 490)

Y2 = tk.Label(root, text="Y")  # 标签
Y2.place(x = 265,y = 520)
Y22 = tk.Text(root,width=9, height=1, undo=True, autoseparators=False)
Y22.place(x = 280,y = 520)

L2 = tk.Label(root, text="L")  # 标签
L2.place(x = 370,y = 490)
L22 = tk.Text(root,width=9, height=1, undo=True, autoseparators=False)
L22.place(x = 385,y = 490)

T2 = tk.Label(root, text="T")  # 标签
T2.place(x = 370,y = 520)
T22 = tk.Text(root,width=9, height=1, undo=True, autoseparators=False)
T22.place(x = 385,y = 520)

J = tk.Text(root,width=30, height=7, undo=True, autoseparators=False)        #记录过程点
J.place(x = 530,y = 490)





v1 = tk.IntVar()            # 用来表示按钮是否选中
v2 = tk.IntVar()
c1 = tk.Checkbutton(root, text='顺圆', variable=v1).place(x = 70,y = 138)
c2 = tk.Checkbutton(root, text='逆圆', variable=v2).place(x = 120,y = 138)

#端口
user_text1 = tk.StringVar()
user_text1 = tk.Entry(root, textvariable=user_text1,width=5)  # 创建文本框
user_text1.place(x=75,y=20)
#kduank = tk.Label(root, text=serialName)  # z标签
#kduank.place(x = 75,y = 20)

#波特率
user_text2 = tk.StringVar()
user_text2 = tk.Entry(root, textvariable=user_text2,width=5)  # 创建文本框
user_text2.place(x=75,y=50)
botel = tk.Label(root, text="115200")  # 标签
botel.place(x = 75,y = 50)
#直线坐标
user_text3 = tk.StringVar()
user_text3 = tk.Entry(root, textvariable=user_text3,width=15)  # 创建文本框
user_text3.place(x=75,y=110)
#圆弧半径
user_text4 = tk.StringVar()
user_text4 = tk.Entry(root, textvariable=user_text4,width=15)  # 创建文本框
user_text4.place(x=75,y=170)
#圆弧起点
user_text5 = tk.StringVar()
user_text5 = tk.Entry(root, textvariable=user_text5,width=15)  # 创建文本框
user_text5.place(x=75,y=200)

v3 = tk.IntVar()            # 用来表示按钮是否选中
v4 = tk.IntVar()
c3 = tk.Checkbutton(root, text='直线', variable=v3).place(x = 55,y = 228)
c4 = tk.Checkbutton(root, text='圆弧', variable=v4).place(x = 105,y = 228)



# 设置选择按钮
def draw_orignalline(xo, yo, xe, ye):  # 绘制理想曲线
    turtle.speed(10)
    turtle.pencolor("#6495ED")
    turtle.width(3)
    turtle.penup()
    turtle.goto(xo, yo)
    turtle.pendown()
    turtle.goto(xe, ye)
    turtle.penup()
    turtle.goto(xo, yo)

def draw_coordinate():   # 绘制坐标线
    turtle.pencolor("#000000")
    for i in range(40):
        canvas.create_line(-500, int(10 * i), 500, int(10 * i), dash=1, width=1, )
        canvas.create_line(-500, -int(10 * i), 500, -int(10 * i), dash=1, width=1, )
        canvas.create_line(int(10 * i), -500, int(10 * i), 500, dash=1, width=1,)
        canvas.create_line(-int(10 * i), -500, -int(10 * i), 500, dash=1, width=1, )
    canvas.create_line(-500, 0, 500, 0, fill='black', width=3)
    canvas.create_line(0, 500, 0, -500, fill='black', width=3)

def getuser():  # 该函数用来获得文本框内容
    user = user_text3.get()  # 获取文本框内容
    return user

def getuser1():  # 该函数用来获得文本框内容
    user2 = user_text5.get()  # 圆弧起终点坐标
    return user2

def getTheta(x,y):
    T = 0
    if (x > 0) and (y > 0):  # 第一象限
        T = eval("%.3f"%math.degrees(math.atan(y/x)))
    elif (x < 0) and (y > 0):  # 第二象限
        T = eval("%.3f"%math.degrees(math.atan(y/x))) +180
    elif (x < 0) and (y < 0):  # 第三象限
        T = 180+eval("%.3f"%math.degrees(math.atan(y/x)))
    elif (x > 0) and (y < 0):  # 第四象限
        T = eval("%.3f"%math.degrees(math.atan(y/x)))+360
    elif x > 0 and y == 0:
        T = 0
    elif x < 0 and y == 0:
        T = 180
    elif x == 0 and y > 0:
        T = 90
    elif x == 0 and y < 0:
        T = 270
    return T

def get_style():
    v_3 = v3.get()
    v_4 = v4.get()
    return v_3, v_4

def get_style1():
    v_1 = v1.get()
    v_2 = v2.get()
    return v_1, v_2

def get_style2():
    v_5 = v5.get()
    v_6 = v6.get()
    return v_5, v_6

#[(20,20),(-20,16)]
def draw_line():
    line_path = eval(getuser())
    for i in range(len(line_path)-1):
        x0 = line_path[i][0]
        y0 = line_path[i][1]
        xe = line_path[i+1][0]
        ye = line_path[i+1][1]
        draw_orignalline(x0*beishu, y0*beishu, xe*beishu, ye*beishu)
        draw_Line(x0, y0, xe, ye)


def draw_Circle():
    r = eval(user_text4.get())
    points = eval(getuser1())
    shun, ni = get_style1()
    x0 = points[0][0]
    y0 = points[0][1]
    xe = points[1][0]
    ye = points[1][1]
    if shun == 1 and ni == 0:
        sn = 1
        draw_circle(x0,y0,xe,ye,r,sn)
    elif shun == 0 and ni == 1:
        sn = 0
        draw_circle(x0,y0,xe,ye,r,sn)
    else:
        print("！！请检查输入！！")



def check():
    points = []
    contents = biancheng.get('1.0', END)
    #print(contents)
    with open("C.txt","w") as f:
        f.write(contents)
    f.close()
    with open("C.txt", "r") as f:
        for line in f.readlines():
            fenduan = {'Case': 'L', 'X': 0, 'Y': 0, 'R': 0,'sn':0}
            an = line.replace(" ", "")
            #print(an)
            if "G01" in an:
                fenduan["Case"] = "L"
                X = an.index("X")
                Y = an.index("Y")
                x = eval(an[X+1:Y:1])
                fenduan["X"] = x
                if "F" in an:
                    F = an.index("F")
                    y = eval(an[Y+1:F:1])
                    fenduan["Y"] = y
                else:
                    y = eval(an[Y+1:-1:1])
                    fenduan["Y"] = y
                points.append(fenduan)
            if "G02" in an:
                fenduan["Case"] = "C"
                X = an.index("X")
                Y = an.index("Y")
                R = an.index("R")
                x = eval(an[X + 1:Y:1])
                y = eval(an[Y + 1:R:1])
                fenduan["X"] = x
                fenduan["Y"] = y
                fenduan["sn"] = 1
                if "F" in an:
                    F = an.index("F")
                    r = eval(an[R+1:F:1])
                    fenduan["R"] = r
                else:
                    r = eval(an[R+1:-1:1])
                    fenduan["R"] = r
                points.append(fenduan)
            if "G03" in an:
                fenduan["Case"] = "C"
                X = an.index("X")
                Y = an.index("Y")
                R = an.index("R")
                x = eval(an[X + 1:Y:1])
                y = eval(an[Y + 1:R:1])
                fenduan["X"] = x
                fenduan["Y"] = y
                fenduan["sn"] = 0
                if "F" in an:
                    F = an.index("F")
                    r = eval(an[R + 1:F:1])
                    fenduan["R"] = r
                else:
                    r = eval(an[R + 1:-1:1])
                    fenduan["R"] = r
                points.append(fenduan)
        f.close()
        print(points)
    x0,y0 = points[0]["X"],points[0]["Y"]
    for i in range(1,len(points)):
        if points[i]["Case"] == "L":
            xe,ye = points[i]["X"],points[i]["Y"]
            draw_Line(x0, y0, xe, ye)
            x0, y0 = points[i]["X"], points[i]["Y"]
        if points[i]["Case"] == "C":
            xe, ye = points[i]["X"], points[i]["Y"]
            R = points[i]["R"]
            sn = points[i]["sn"]
            draw_circle(x0, y0, xe, ye,R,sn)
            x0, y0 = points[i]["X"], points[i]["Y"]

def get_place():
    l = eval(L22.get('1.0', END))
    t = eval(T22.get('1.0', END))
    return l,t



def nishiz(): #点动控制  N为逆时针转动，S为顺时针，G为伸长，D为缩短
    global point
    k,g = get_style2()
    if k == 0 and g == 0 :
        send_msg("N" + "\r\n")  # 写数据
    elif k == 1 and g == 0 :
        l,t = get_place()
        send_msg("N" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        t += 10
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["N"] += 1
        point = (x,y)
    else:
        l, t = get_place()
        send_msg("F" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        t += 1
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["N"] += 1
        point = (x, y)


def shunshiz():
    k,g = get_style2()
    global point
    if k == 0 and g == 0 :
        send_msg("S" + "\r\n")  # 写数据
    elif k == 1 and g == 0 :
        l, t = get_place()
        #点动控制  N为逆时针转动，S为顺时针，G为伸长，D为缩短
        send_msg("S" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        t -= 10
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["S"] += 1
        point = (x,y)
    else:
        l, t = get_place()
        # 点动控制  N为逆时针转动，S为顺时针，G为伸长，D为缩短
        send_msg("A" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        t -= 1
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["S"] += 1
        point = (x, y)


def shenc():                    #点动控制  N为逆时针转动，S为顺时针，G为伸长，D为缩短
    global point
    k,g = get_style2()
    if k == 0 and g == 0 :
        send_msg("G" + "\r\n")  # 写数据
    elif k == 1 and g == 0 :
        l, t = get_place()
        send_msg("G" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        l += 4
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["G"] += 1
        point = (x,y)
    else:
        l, t = get_place()
        send_msg("W" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        l += 1
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["G"] += 1
        point = (x, y)


def suod():                    #点动控制  N为逆时针转动，S为顺时针，G为伸长，D为缩短
    global point
    k,g = get_style2()
    if k == 0 and g == 0 :
        send_msg("D" + "\r\n")  # 写数据
    elif k == 1 and g == 0 :
        l, t = get_place()
        send_msg("D" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        l -= 4
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["D"] += 1
        point = (x,y)

    else:
        l, t = get_place()
        send_msg("X" + "\r\n")  # 写数据
        T22.delete(1.0, END)
        L22.delete(1.0, END)
        X22.delete(1.0, END)
        Y22.delete(1.0, END)
        l -= 1
        x = eval("%.6f" % (l * math.cos(math.radians(t))))
        y = eval("%.6f" % (l * math.sin(math.radians(t))))
        X22.insert('end', x)
        Y22.insert('end', y)
        L22.insert('end', l)
        T22.insert('end', str(t))
        shi["D"] += 1
        point = (x, y)




def sure():
    global point
    x =  eval(X1.get())
    y =  eval(Y1.get())
    point = (x,y)
    pointss.append(point)
    Theta0 = getTheta(x,y)
    L1.insert('end', eval("%.3f"%(pow(x**2+y**2,0.5))))
    T1.insert('end', str(Theta0))
    X22.insert('end', x)
    Y22.insert('end', y)
    L22.insert('end', eval("%.3f"%(pow(x**2+y**2,0.5))))
    T22.insert('end', str(getTheta(x,y)))
    J.insert('end',"第1个点"+str(point)+"\n")


def huiling():
    send_msg("H" + "\r\n")  # 写数据

def add():
    global number
    pointss.append(point)
    J.insert('end', "第{}个点".format(number) + str(point) + "\n")
    number += 1
def delete():
    global pointss
    shi["S"] = 0
    shi["N"] = 0
    shi["G"] = 0
    shi["D"] = 0
    pointss = []
    T22.delete(1.0, END)
    L22.delete(1.0, END)
    X22.delete(1.0, END)
    Y22.delete(1.0, END)
    L1.delete(1.0, END)
    T1.delete(1.0, END)
    J.delete(1.0, END)
    print(pointss)

def shijiao():
    global pointss
    print(pointss)
    a = pointss[::-1]
    for i in range(len(a) - 1):
        x0 = a[i][0]
        y0 = a[i][1]
        xe = a[i + 1][0]
        ye = a[i + 1][1]
        draw_orignalline(x0 * beishu, y0 * beishu, xe * beishu, ye * beishu)
        draw_Line(x0, y0, xe, ye)
    for i in range(len(pointss) - 1):
        x0 = pointss[i][0]
        y0 = pointss[i][1]
        xe = pointss[i + 1][0]
        ye = pointss[i + 1][1]
        draw_orignalline(x0 * beishu, y0 * beishu, xe * beishu, ye * beishu)
        draw_Line(x0, y0, xe, ye)
    print(pointss)


def whole():
    line, circle = get_style()
    if line == 1 and circle == 0:
        print(1+1)
        print(eval(getuser()))
        draw_line()

    elif line == 0 and circle == 1:
        draw_Circle()
    else:
        print("！！请检查输入！！")

def openn():
    open_ser()

def close():
    close_ser()

def clear():
    turtle.clear()
    huiling()

tk.Button(master=root, text="开始插补", command=whole).place(x = 35,y = 260)
tk.Button(master=root, text="回零操作", command=clear).place(x = 110,y = 260)
tk.Button(master=root, text="  伸  ", command=shenc).place(x = 80,y = 310)
tk.Button(master=root, text="  缩  ", command=suod).place(x = 80,y = 390)
tk.Button(master=root, text="  顺  ", command=shunshiz).place(x = 40,y = 350)
tk.Button(master=root, text="  逆  ", command=nishiz).place(x = 120,y = 350)
tk.Button(master=root, text="  开  ", command=openn).place(x = 40,y = 310)
tk.Button(master=root, text="  关  ", command=close).place(x = 120,y = 310)
tk.Button(master=root, text="开始编程", command=check).place(x = 720,y = 410)
tk.Button(master=root, text="确    认", command=sure).place(x = 70,y = 550)
tk.Button(master=root, text="添加当前点", command=add).place(x = 330,y = 550)
tk.Button(master=root, text="开启示教模式", command=shijiao).place(x = 760,y = 550)
tk.Button(master=root, text="  复位  ", command=delete).place(x = 775,y = 510)


draw_coordinate()
tk.mainloop()
#[(100,-20),(0,100)]