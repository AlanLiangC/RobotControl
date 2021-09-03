import math
import numpy as np
from pylab import *
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
def judge_quadrant(x0, y0, xe, ye):
    if (x0 == 0 and y0 == 0) or (xe == 0 and ye == 0) or (y0*xe == ye*x0):
        sn = 2
    else:
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
            if y0 > 0:
                sn = 1
            else:
                sn = 0
        elif x < 0 and y == 0:
            if y0 > 0:
                sn = 0
            else:
                sn = 1
            #quadrant = 6  # X轴负方向
        elif x == 0 and y > 0:
            if x0 > 0:
            #quadrant = 5  # X轴正方向
                sn = 0
            else:
                sn = 1
        elif x == 0 and y < 0:
            if x0 > 0:
            #quadrant = 5  # X轴正方向
                sn = 1
            else:
                sn = 0
    return sn
def CircleCenter(x0,y0,xe,ye,R,sn):    #sn  1顺圆0逆圆
    ln = []
    l = []
    lpoint = ((ye - y0) ** 2 + (xe - x0) ** 2) ** 0.5  # 两点之间的距离
    theta = math.degrees(math.acos(lpoint ** 2 / (2 * R * lpoint)))  # 两线段的夹角
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
                        ln = point
                        break
            else :
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a < 0 :
                        ln = point
                        break
        elif R < 0 :
            if sn == 0:
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a < 0 :

                        ln = point
                        break
            else :
                for point in l :
                    a = (x0-point[0])*(ye-point[1]) - (y0-point[1])*(xe-point[0])
                    if a > 0 :
                        ln = point
                        break
    if xe == x0 :
        if ye - y0 > 0:
            if sn == 0:
                ln = [x0 - abs(R*math.sin(math.radians(theta))),(ye + y0)/2]
            else:
                ln = [x0 + abs(R*math.sin(math.radians(theta))), (ye + y0) / 2]
        else:
            if sn == 0:
                ln = [x0 + abs(R*math.sin(math.radians(theta))),(ye+y0)/2]
            else:
                ln = [x0 - abs(R*math.sin(math.radians(theta))), (ye + y0) / 2]

    if ye == y0:
        if xe - x0 > 0:
            if sn == 0:
                ln = [(xe+x0)/2,y0 + abs(R*math.sin(math.radians(theta)))]
            else:
                ln = [(xe+x0)/2,y0 - abs(R*math.sin(math.radians(theta)))]
        else:
            if sn == 0:
                ln = [(xe+x0)/2,y0 - abs(R*math.sin(math.radians(theta)))]
            else:
                ln = [(xe+x0)/2,y0 + abs(R*math.sin(math.radians(theta)))]
    print(ln)
    return ln

def cirspeed(x0, y0, xe, ye, v0, N, time_step,r,circle = []):
    x0 = x0 - circle[0]
    y0 = y0 - circle[1]
    xe = xe - circle[0]
    ye = ye - circle[1]
    lpoint = ((ye - y0) ** 2 + (xe - x0) ** 2) ** 0.5  # 两点之间的距离
    LE = (ye ** 2 + xe ** 2) ** 0.5  # 终点线段的长度
    Lo = (y0**2+x0**2)**0.5                 #起点线段长度
    theta = math.degrees(math.acos((2 * r**2 - lpoint ** 2) / (2 * r**2)))
    omg = abs(180*v0/(math.pi*r))

    if r > 0:
        theta = theta
    else:
        theta = 360 - theta
    print(theta)
    jiasu = np.array([])
    ans = np.array([])
    n = int((theta / omg) // time_step)
    print(n)
    omg = theta / (n * time_step)
    for i in range(1, N + 1):
        step = eval("%.6f"%((omg * i ** 2 * time_step - omg * (i - 1) ** 2 * time_step) / (2 * N)))
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
def get_cirpoint(x0,y0,xe,ye,r,sn,ans = [],circle=[]):
    points = np.array([[],[]])
    points = np.append(points,[[x0],[y0]],axis = 1)
    Theta0 = getTheta(x0-circle[0], y0-circle[1])
    the  = ans[::1]
    for i in range(1,the.shape[0]):
        the[i] = the[i] + the[i-1]
    #print(the)
    plt.figure(2)
    plt.title("旋转轴转角")
    plt.xlabel("Time")
    plt.ylabel("角度（角度制）")
    t = [time_step*i for i in range(the.shape[0])]
    plt.plot(t, the, "*")
    if sn == 0:
        for i in range(the.shape[0]):
            x = eval("%.7f"%(circle[0]+r*math.cos(math.radians(Theta0+the[i]))))
            y = eval("%.7f"%(circle[1]+r*math.sin(math.radians(Theta0+the[i]))))
            points = np.append(points,[[x],[y]],axis=1)
    else:
        for i in range(the.shape[0]):
            x = eval("%.7f"%(circle[0] + abs(r) * math.cos(math.radians(Theta0 - the[i]))))
            y = eval("%.7f"%(circle[1] + abs(r) * math.sin(math.radians(Theta0 - the[i]))))
            points = np.append(points,[[x],[y]],axis=1)
    #print(points)
    plt.figure(3)
    plt.title("粗插补采样点")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(points[0], points[1], "*")
    #plt.show()
    return points

def getheta(points):
    the = np.array([])
    for i in range(points.shape[1]-1):
        Lo = (points[0][i] ** 2 + points[1][i] ** 2) ** 0.5  # 起点线段长度
        lpoint = ((points[1][i+1] - points[1][i]) ** 2 + (points[0][i+1] - points[0][i]) ** 2) ** 0.5  # 两点之间的距离
        LE = (points[0][i+1] ** 2 + points[1][i+1] ** 2) ** 0.5  # 终点线段的长度
        theta = math.degrees(math.acos((Lo ** 2 + LE ** 2 - lpoint ** 2) / (2 * Lo * LE)))  # 两线段的夹角
        the = np.append(the,theta)
    #print(the)
    return the

def draw_omg(time_step,Theta_step,theta):
    tim = np.array([])
    omg = np.array([])
    jicun = np.array([])
    jicun = np.append(jicun,0)
    yushu = 0
    print(theta)
    plt.figure(4)
    for i in range(theta.shape[0]) :
        tim = np.append(tim,i*time_step)
        omg = np.append(omg,theta[i]/time_step)
    plt.title("角速度（连续）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    plt.plot(tim,omg, "*")
    #plt.show()
    #print(tim,omg)
    for the in theta :
        n = int((the+yushu) // Theta_step)
        yushu = the+yushu - n*Theta_step
        jicun = np.append(jicun,n)

    return jicun
    #jicun.append(0)
    '''plt.figure(5)
    plt.title("角速度（脉冲）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    for i in range(jicun.shape[0]-1):
        plt.plot((i * time_step,i * time_step ),(jicun[i] * Theta_step / time_step, jicun[i+1] * Theta_step / time_step), "-")
        #plt.plot((i * time_step, (i+1) * time_step),(jicun[i+1] * Theta_step / time_step, jicun[i+1] * Theta_step / time_step), "-")
    plt.plot(((jicun.shape[0]-1)*time_step,(jicun.shape[0]-1)*time_step),(jicun[-1] * Theta_step / time_step,0))
'''
    #print(jicun)
    #print(jicun.shape[0])

    '''plt.figure(5)
    plt.title("角速度（脉冲）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    for i in range(jicun.shape[0]-1):
        plt.plot((i * time_step,i * time_step ),(jicun[i] * Theta_step / time_step, jicun[i+1] * Theta_step / time_step), "-")
        plt.plot((i * time_step, (i+1) * time_step),(jicun[i+1] * Theta_step / time_step, jicun[i+1] * Theta_step / time_step), "-")
    plt.plot(((jicun.shape[0]-1)*time_step,(jicun.shape[0]-1)*time_step),(jicun[-1] * Theta_step / time_step,0))'''


def get_number(time_step, l_step, points):
    tim = np.array([])
    v = np.array([])
    jicun = np.array([])
    jicun = np.append(jicun,0)
    yushu = 0
    speed = np.array([])
    speed = np.append(speed,0)
    for i in range(points.shape[1]-1):
        x0 = points[0][i]
        y0 = points[1][i]
        xe = points[0][i + 1]
        ye = points[1][i + 1]
        # Address = cross_point(x0,y0,xe,ye)
        Lo = (y0 ** 2 + x0 ** 2) ** 0.5  # 起点线段长度
        LE = (ye ** 2 + xe ** 2) ** 0.5  # 终点线段的长度
        lpoint = ((ye - y0) ** 2 + (xe - x0) ** 2) ** 0.5  # 两点之间的距离
        speed = np.append(speed,(LE - Lo) / time_step)
        # Lmin = ((Address[0]) ** 2 + (Address[1]) ** 2) ** 0.5  # 垂线的距离
        '''if (min(xe, x0) <= Address[0] <= max(xe, x0)) and (min(ye, y0) <= Address[1] <= max(ye, y0)):
            number1 = int((abs(Lo - Lmin)+yushu) // l_step)
            yushu = abs(Lo - Lmin)+yushu-number1*l_step

            number2 = int((abs(LE - Lmin)-yushu) // l_step)
            number = int((abs(Lo - Lmin)) // l_step + (abs(LE - Lmin)) // l_step)
        else:'''
        number = int((abs(Lo - LE) + yushu) // l_step)
        yushu = abs(Lo - LE) + yushu - number * l_step
        if Lo - LE >= 0:
            jicun = np.append(jicun,-number)
        else:
            jicun = np.append(jicun,number)
            # print(Lo - LE)
            # print(number)
    speed = np.append(speed,0)
    plt.figure(6)
    for i in range(speed.shape[0]):
        tim = np.append(tim,i * time_step)
        v = np.append(v,speed[i] / time_step)
    plt.title("线速度（连续）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    plt.plot(tim, v, "*")

    '''plt.figure(7)
    plt.title("线速度（脉冲）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    for i in range(jicun.shape[0] - 1):
        plt.plot((i * time_step, i * time_step),
                 (jicun[i] * l_step / time_step, jicun[i + 1] * l_step / time_step), "-")
        plt.plot((i * time_step, (i + 1) * time_step),
                 (jicun[i + 1] * l_step / time_step, jicun[i + 1] * l_step / time_step), "-")
    plt.plot(((jicun.shape[0] - 1) * time_step, (jicun.shape[0] - 1) * time_step), (jicun[-1] * l_step / time_step, 0))'''

    # plt.show()
    #print(jicun)
    print(jicun.shape)
    return jicun



    # print(jicun)


def get_circle(x0,y0,xe,ye,r,sn):
    an = judge_quadrant(x0, y0, xe, ye)

    l = np.array([])
    liang= CircleCenter(x0,y0,xe,ye,r,sn)
    ans = cirspeed(x0,y0,xe,ye,v0,num,time_step,r,liang)
    points = get_cirpoint(x0,y0,xe,ye,r,sn,ans,liang)
    #print(points)
    the = getheta(points)
    ao = draw_omg(time_step,Theta_step,the)
    #l = get_number(time_step, L_step, points)
    #l = np.append(l,ao)
    #print(ao)
    #print(ao.shape)
    #plt.show()
    if (an):
        for i in range(ao.shape[0]):
            ao[i] = -ao[i]
    if liang[0] == 0 and liang[1] == 0:
        for i in range(ao.shape[0]):
            l = np.append(l,0)
    else:
        l = get_number(time_step, L_step, points)
    plt.show()

    ao = np.append(ao,l)
    #return y,points
    #print(l)
    #print(ao)
    print(ao.shape)
    #print(the)
    return ao

#get_circle(50,100,100,50,-50,0)
