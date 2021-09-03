# -*- coding:utf-8 -*-
import turtle
import tkinter as tk
import math
from PointAdd import cross_point
from Findmin import find_point
from Distance import distance
from Val_speed import *
from JZB import *
root = tk.Tk()
root.title('数控插补演示界面')
canvas = tk.Canvas(master=root, bd=5, width =850, height =850)
canvas.pack()
turtle = turtle.RawTurtle(canvas)
turtle.hideturtle()
color_1 = (0, 191, 255)
color_2 = (255, 181, 197)
my_step = 20                #步长倍率
Theta_step = 0.18          #转角脉冲当量
L_step = 1*my_step       #伸缩脉冲当量
time_step = 0.1             #粗插补采样周期
#acc = 0.5*my_step          #粗插补采样步长
num = 10                    #加速时间
v0 = 10*my_step
sn = 0          #判断逆时针顺时针 0为逆时针 1为顺时针
way = 0
T = 0
rout = []

l1 = tk.Label(root, text="输入坐标 格式[(x0,y0),(x1,y1)...(xn,yn)]")  # 标签
l1.pack(side=tk.LEFT)  # 指定包管理器放置组件
user_text = tk.StringVar()
user_text = tk.Entry(root, textvariable=user_text,width=25)  # 创建文本框
user_text.pack(side=tk.LEFT)
# 设置选择按钮
v1 = tk.IntVar()            # 用来表示按钮是否选中
v2 = tk.IntVar()
c1 = tk.Checkbutton(root, text='直线', variable=v1).pack(side=tk.LEFT)
c2 = tk.Checkbutton(root, text='圆', variable=v2).pack(side=tk.LEFT)

#绘制坐标
def draw_coordinate():   # 绘制坐标线
    turtle.pencolor("#000000")
# 这里是画虚线
    for i in range(40):
        canvas.create_line(-500, int(20 * i), 500, int(20 * i), dash=1, width=1, )
        canvas.create_line(-500, -int(20 * i), 500, -int(20 * i), dash=1, width=1, )
        canvas.create_line(int(20 * i), -500, int(20 * i), 500, dash=1, width=1,)
        canvas.create_line(-int(20 * i), -500, -int(20 * i), 500, dash=1, width=1, )
# 绘制坐标轴
    canvas.create_line(-500, 0, 500, 0, fill='black', width=3)
    canvas.create_line(0, 500, 0, -500, fill='black', width=3)
#象限判断
def judge_quadrant(x0, y0, xe, ye):
    if xe-x0 != 0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键

    x = xe - x0
    y = ye - y0
    if (x > 0) and (y > 0):  # 第一象限
        #quadrant = 1
        if b1 > 0 :
            sn = 1              #顺时针
        else:
            sn = 0              #逆时针
    elif (x < 0) and (y > 0):  # 第二象限
        #quadrant = 2
        if b1 > 0 :
            sn = 0              #逆时针
        else:
            sn = 1              #顺时针
    elif (x < 0) and (y < 0):  # 第三象限
        #quadrant = 3
        if b1 > 0 :
            sn = 0              #逆时针
        else:
            sn = 1              #顺时针
    elif (x > 0) and (y < 0):  # 第四象限
        #quadrant = 4
        if b1 > 0 :
            sn = 1              #顺时针
        else:
            sn = 0              #逆时针
    elif x > 0 and y == 0:
        #quadrant = 5  # X轴正方向
        sn = 1
    elif x < 0 and y == 0:
        #quadrant = 6  # X轴负方向
        sn = 0
    elif x == 0 and y > 0:
        #quadrant = 7  # Y轴正方向
        sn = 0
    elif x == 0 and y < 0:
        #quadrant = 8  # Y轴负方向
        sn = 1
    return sn

#转换端点角度
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

def interpolation(sn,x0, y0, xe, ye):
    global point
    Address = cross_point(x0,y0,xe,ye)
    point = [(x0, y0)]
    Theta = []
    L = []
    Lo = (y0**2+x0**2)**0.5                 #起点线段长度
    l = Lo
    l_time = Lo
    lpoint = ((ye-y0)**2+(xe-x0)**2)**0.5  #两点之间的距离
    LE = (ye**2+xe**2)**0.5                #终点线段的长度
    Lmin = ((Address[0])**2 + (Address[1])**2)**0.5   #垂线的距离
    Theta0 = getTheta(x0,y0)
    the = Theta0
    theta = math.degrees(math.acos((Lo**2+LE**2-lpoint**2)/(2*Lo*LE)))   #两线段的夹角
    if (min(xe,x0) <= Address[0] <= max(xe,x0)) and  (min(ye,y0) <= Address[1] <= max(ye,y0)):
        number = int(theta // Theta_step + (abs(Lo - Lmin)) // L_step + (abs(LE - Lmin)) // L_step)
        way = 1
    else:
        number = int(theta // Theta_step + (abs(Lo - LE)) // L_step)
        way = 0
    Theta.append(the)
    L.append(Lo)
    cnt = 0
    ant = 0
    turtle.speed(10)
    turtle.pencolor("#FFC0CB")
    turtle.width(3)
    turtle.goto(point[0])
    turtle.pendown()
    while cnt < number+2 :
        if sn == 0 :            #逆时针
            if way == 1 :
                add = find_point(Theta0, Theta_step, sn, theta, x0, y0, xe, ye)
                if ant <= add :
                    if l_time >= l:
                        l_time -= L_step
                        point.append((l_time*math.cos(math.radians(the)),l_time*math.sin(math.radians(the))))
                        turtle.goto((l_time*math.cos(math.radians(the)),l_time*math.sin(math.radians(the))))
                        rout.append(-1)
                    else:
                        the += Theta_step
                        turtle.setheading(the+90)
                        turtle.circle(l_time, Theta_step)
                        l = float(distance(the,x0,y0,xe,ye))
                        Theta.append(the)
                        rout.append(0)
                        ant += 1
                else:
                    if l_time <= l:
                        l_time += L_step
                        point.append((l_time * math.cos(math.radians(the)), l_time * math.sin(math.radians(the))))
                        turtle.goto((l_time*math.cos(math.radians(the)),l_time*math.sin(math.radians(the))))
                        rout.append(1)

                    else:
                        the += Theta_step
                        turtle.setheading(the + 90)
                        turtle.circle(l_time, Theta_step)
                        l = float(distance(the, x0, y0, xe, ye))
                        l = float(distance(the, x0, y0, xe, ye))
                        Theta.append(the)
                        rout.append(0)
        cnt += 1
    #print(rout)
    print(number)
    #print(add)
'''def draw_line(way,sn,track = []):
    turtle.speed(1)
    turtle.pencolor("#FFC0CB")
    turtle.width(3)
    turtle.goto(point[0])
    turtle.pendown()
    if sn == 0 and way == 1:
        for item in track:
            print(item)'''

#获取用户输入
def getuser():  # 该函数用来获得文本框内容
    user = user_text.get()  # 获取文本框内容
    return user

def get_style():
    v_1 = v1.get()
    v_2 = v2.get()
    return v_1, v_2

#绘制初始直线
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

#离散点连线
def draw_points(points = []):
    turtle.speed(10)
    turtle.pencolor("#6495ED")
    turtle.width(1)
    for point in points:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(point[0], point[1])

#绘制所有图像
def draw_whole():
    line, circle = get_style()
    if line == 1 and circle == 0:
        turtle.clear()
        line_path = eval(getuser())
        for i in range(0, len(line_path) - 1):
            xo = line_path[i][0] * my_step
            yo = line_path[i][1] * my_step
            xe = line_path[i + 1][0] * my_step
            ye = line_path[i + 1][1] * my_step
            plt.figure(1)  # 创建一个没有 axes 的 figure
            liang = valespeed(xo, yo, xe, ye, 100, 10, time_step)
            points = getpoints(xo,yo,xe,ye,liang)
            the = getheta(points)
            #print(the)
            draw_points(points)
            draw_orignalline(xo, yo, xe, ye)
            sn = judge_quadrant(xo, yo, xe, ye)
            interpolation(sn, xo, yo, xe, ye)
            #plt.figure(2)  # 创建一个没有 axes 的 figure
            #draw_omg(time_step,the)
            #plt.show()
            #fen = getspeed(Theta_step,the,rout)
            #plt.figure(3)  # 创建一个没有 axes 的 figure
            #get_paint(L_step,time_step,fen)
            #plt.show()
            #print(points)
            #print(the)
            #print(rout)





    elif line == 0 and circle == 1:
        print("你是错的")
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.pencolor("black")
        turtle.goto(10,10)




def clear():
    turtle.clear()
tk.Button(master=root, text="开始绘图", command=draw_whole).pack(side=tk.LEFT)
tk.Button(master=root, text="清除图形", command=clear).pack(side=tk.LEFT)
print(getuser())
draw_coordinate()  # 绘制坐标先
tk.mainloop()

