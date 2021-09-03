import math
import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
from Val_speed import draw_omg
from Val_speed import getheta
from pylab import *
from Line_speed import get_number


mpl.rcParams['font.sans-serif'] = ['SimHei']

Theta_step = 0.01          #转角脉冲当量
L_step = 0.002               #伸缩脉冲当量
time_step = 0.02             #粗插补采样周期
num = 5                    #加速次数
v0 = 5                     #匀速
sn = 0          #判断逆时针顺时针 0为逆时针 1为顺时针
way = 0
T = 0
rout = []

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



#获得圆心
def CircleCenter(x0,y0,xe,ye,R,sn):    #sn  1顺圆0逆圆
    ln = []
    l = []
    if xe - x0 != 0:
        c1 = (xe*xe - x0*x0 + ye*ye - y0*y0) / (2 *(xe - x0))
        c2 = (ye - y0) / (xe - x0)
        A = (c2*c2 + 1)
        B = (2 * x0*c2 - 2 * c1*c2 - 2 * y0)
        C = x0*x0 - 2 * x0*c1 + c1*c1 + y0*y0 - R*R

        y1 = (-B + pow((B*B - 4 * A*C),0.5)) / (2 * A)
        x1 = c1 - c2 * y1
        y2 = (-B - pow((B * B - 4 * A * C), 0.5)) / (2 * A)
        x2 = c1 - c2 * y2

        l.append([x1,y1])
        l.append([x2,y2])
        if R > 0 :
            if sn == 0:
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a > 0 :
                        print(point)
                        ln = point
                        break
            else :
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a < 0 :
                        print(point)
                        ln = point
                        break
        elif R < 0 :
            if sn == 0:
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a < 0 :
                        print(point)
                        ln = point
                        break
            else :
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a > 0 :
                        print(point)
                        ln = point
                        break
    else :
        if ye - y0 > 0:
            if sn == 0:
                ln = [x0 - abs(R),(ye+y0)/2]
            else:
                ln = [x0 + abs(R), (ye + y0) / 2]
        else:
            if sn == 0:
                ln = [x0 + abs(R),(ye+y0)/2]
            else:
                ln = [x0 - abs(R), (ye + y0) / 2]
    return ln

#获得每段小距离
def cirspeed(x0, y0, xe, ye, v0, N, time_step,r,circle = []):
    x0 = x0 - circle[0]
    y0 = y0 - circle[1]
    xe = xe - circle[0]
    ye = ye - circle[1]
    omg = 180*v0/(math.pi*r)
    lpoint = ((ye - y0) ** 2 + (xe - x0) ** 2) ** 0.5  # 两点之间的距离
    LE = (ye ** 2 + xe ** 2) ** 0.5  # 终点线段的长度
    Lo = (y0**2+x0**2)**0.5                 #起点线段长度
    theta = math.degrees(math.acos((Lo ** 2 + LE ** 2 - lpoint ** 2) / (2 * Lo * LE)))
    if r > 0:
        theta = theta
    else:
        theta = 360 - theta
    jiasu = np.array([])
    ans = np.array([])
    n = int((theta / omg) // time_step)
    omg = theta / (n * time_step)
    for i in range(1, N + 1):
        step = eval("%.4f"%((omg * i ** 2 * time_step - omg * (i - 1) ** 2 * time_step) / (2 * N)))
        jiasu = np.append(jiasu,step)
    cishu = n - N
    yunsu = np.array([omg * time_step for i in range(cishu)])
    ans = np.append(ans,jiasu)
    ans = np.append(ans,yunsu)
    jiansu = jiasu[::-1]
    ans = np.append(ans,jiansu)
    plt.figure(1)
    plt.title("末端速度理想曲线")
    plt.xlabel("时间")
    plt.ylabel("速度")
    plt.plot([0, N * time_step, n * time_step, (n + N) * time_step], [0, omg, omg, 0], "-")
    #print(ans)
    #print(ans.shape)
    return ans
#取得粗插补点集

#取得粗插补点集
def get_cirpoint(x0,y0,xe,ye,r,sn,ans = [],circle=[]):
    points = []
    points.append((x0,y0))
    Theta0 = getTheta(x0-circle[0], y0-circle[1])
    the = ans
    for i in range(1,len(the)):
        the[i] = the[i] + the[i-1]
    #print(the)

    plt.figure(2)
    plt.title("旋转轴转角")
    plt.xlabel("Time")
    plt.ylabel("角度（角度制）")
    t = [time_step*i for i in range(len(the))]
    plt.plot(t, the, "*")

    if sn == 0:
        for i in range(len(the)):
            x = circle[0]+r*math.cos(math.radians(Theta0+the[i]))
            y = circle[1]+r*math.sin(math.radians(Theta0+the[i]))
            points.append((x,y))


    else:
        for i in range(len(the)):
            x = circle[0] + abs(r) * math.cos(math.radians(Theta0 - the[i]))
            y = circle[1] + abs(r) * math.sin(math.radians(Theta0 - the[i]))
            points.append((x,y))

    #print(points)

    plt.figure(3)
    plt.title("粗插补采样点")
    plt.xlabel("X")
    plt.ylabel("Y")
    for point in points:
        plt.plot(point[0], point[1], "*")

    return points


def get_circle(x0,y0,xe,ye,r,sn):
    l = []
    #x0,y0,xe,ye = eval(input("请输入圆弧段的起始点："))
    #r,sn = eval(input("请输入圆弧的半径（0：逆圆；1：顺圆）："))
    liang= CircleCenter(x0,y0,xe,ye,r,sn)
    #print(liang,sn)
    #print(CircleCenter(4,3,3,4,1,0))
    ans = cirspeed(x0,y0,xe,ye,v0,num,time_step,r,liang)
    points = get_cirpoint(x0,y0,xe,ye,r,sn,ans,liang)
    #print(points)
    the = getheta(points)
    ao = draw_omg(time_step,Theta_step,the)
    if (sn):
        for i in range(len(ao)):
            ao[i] = -ao[i]
    if liang[0] == 0 and liang[1] == 0:
        for i in range(len(ao)):
            l.append(0)
    else:
        l = get_number(time_step, L_step, points)
    plt.show()
    y = ao + l
    print(len(ao))
    #return y,points

get_circle(0,10,10,0,10,1)