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

def valespeed(x0,y0,xe,ye,v0,N,time_step):
    lz=eval("%.4f"%(((xe-x0)**2+(ye-y0)**2)**0.5))
    time1 = lz/v0
    jiasu = np.array([])
    ans = np.array([])
    n = int((lz/v0)//time_step)
    v0 = lz / (n*time_step)
    for i in range(1,N+1):
        jiasu = np.append(jiasu,eval("%.4f"%((v0*i**2*time_step-v0*(i-1)**2*time_step)/(2*N))))
    cishu = n-N
    yunsu = np.array([v0 * time_step for i in range(cishu)])
    ans = np.append(ans, jiasu)
    ans = np.append(ans, yunsu)
    jiansu = jiasu[::-1]
    ans = np.append(ans,jiansu)

    '''for i in range(len(ans)):
        x.append((2**0.5/2)*ans[i])
        y.append((2**0.5/2)*ans[i])

    x[0] = x[0] + 1
    y[0] = y[0] + 2
    for i in range(1,len(x)):
        x[i] = x[i] + x[i-1]
        y[i] = y[i] + y[i-1]'''
    plt.figure(1)
    plt.title("末端速度理想曲线")
    plt.xlabel("时间")
    plt.ylabel("速度")
    plt.plot([0,N*time_step,n*time_step,(n+N)*time_step], [0,v0,v0,0], "-")
    #plt.show()
    '''fig = plt.figure()  # 创建一个没有 axes 的 figure
    plt.title("角速度图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    l = [i for i in range(len(ans))]
    plt.plot([x],[y], "*")
    plt.show()'''
    l = np.array([])
    for i in range(ans.shape[0]):
        l = np.append(l,ans[i])
    for i in range(1,l.shape[0]):
        l[i] = l[i] + l[i-1]

    plt.figure(2)
    plt.title("直线位移")
    plt.xlabel("Time")
    plt.ylabel("角度（角度制）")
    t = [time_step * i for i in range(l.shape[0])]
    plt.plot(t, l, "*")
    #print(ans)
    return ans,time1

def getpoints(x0, y0, xe, ye,step = []):
    points = np.array([[], []])
    points = np.append(points, [[x0], [y0]], axis=1)

    if xe > x0 and ye > y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        #b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x += eval("%.4f"%(math.cos(math.atan(k1))*i))
            y += eval("%.4f"%(math.sin(math.atan(k1))*i))
            points = np.append(points, [[x], [y]], axis=1)

    if xe < x0 and ye > y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x -= eval("%.4f"%(math.cos(math.atan(k1)) * i))
            y -= eval("%.4f"%(math.sin(math.atan(k1)) * i))
            points = np.append(points, [[x], [y]], axis=1)

    if xe < x0 and ye < y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x -= eval("%.4f"%(math.cos(math.atan(k1)) * i))
            y -= eval("%.4f"%(math.sin(math.atan(k1)) * i))
            points = np.append(points, [[x], [y]], axis=1)

    if xe > x0 and ye < y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x += eval("%.4f"%(math.cos(math.atan(k1)) * i))
            y += eval("%.4f"%(math.sin(math.atan(k1)) * i))
            points = np.append(points, [[x], [y]], axis=1)

    if ye - y0 == 0 and xe - x0 > 0 :
        x = x0
        y = y0
        k1 = 0  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        for i in step:
            x += eval("%.4f"%(math.cos(math.atan(k1)) * i))
            y = ye
            points = np.append(points, [[x], [y]], axis=1)

    if ye - y0 == 0 and xe - x0 < 0 :
        x = x0
        y = y0
        k1 = 0  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        for i in step:
            x -= eval("%.4f"%(math.cos(math.atan(k1)) * i))
            y = ye
            points = np.append(points, [[x], [y]], axis=1)

    if ye - y0 > 0 and xe - x0 == 0 :
        x = x0
        y = y0
        for i in step:
            x = xe
            y += i
            points = np.append(points, [[x], [y]], axis=1)

    if ye - y0 < 0 and xe - x0 == 0 :
        x = x0
        y = y0
        for i in step:
            x = xe
            y -= i
            points = np.append(points, [[x], [y]], axis=1)

    '''if (xe,ye) not in points:
        points.append((xe,ye))'''

    plt.figure(3)
    plt.title("粗插补采样点")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(points[0],points[1],"*")
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
    return jicun

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


def get_whole(x0, y0, xe, ye):
    l = np.array([])
    ans ,time1= valespeed(x0,y0,xe,ye,v0,num,time_step)
    sn = judge_quadrant(x0, y0, xe, ye)
    points = getpoints(x0, y0, xe, ye, ans)
    #print(points)
    if sn == 2:
        ao = np.array([])
        l = get_number(time_step, L_step, points)
        for i in range(l.shape[0]):
            ao = np.append(ao,0)
    else:
        the = getheta(points)
        ao = draw_omg(time_step,Theta_step,the)
        l = get_number(time_step, L_step, points)

        if (sn) :
            for i in range(ao.shape[0]):
                ao[i] = -ao[i]
    ao = np.append(ao,l)
    plt.show()
    print(l)

    print(ao)
    print(ao.shape)
    return ao


#get_whole(20,20,-20,16)
#valespeed(0,100,100,0,v0,num,time_step)