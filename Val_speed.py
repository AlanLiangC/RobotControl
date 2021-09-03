import math
import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
l = []
def valespeed(x0,y0,xe,ye,v0,N,time_step):
    a = v0/(N*time_step)
    lz=((xe-x0)**2+(ye-y0)**2)**0.5
    jiasu = []
    ans = []
    n = int((lz/v0)//time_step)
    v0 = lz / (n*time_step)
    for i in range(1,N+1):
        jiasu.append(((v0*i**2*time_step-v0*(i-1)**2*time_step)/(2*N)))
    jiansu = jiasu
    cishu = n-N

    yunsu = [v0*time_step for i in range(cishu)]

    ans.extend(jiasu)
    jiansu.sort(reverse=True)
    ans.extend(yunsu)
    ans.extend(jiansu)
    x = []
    y = []
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
    for i in range(len(ans)):
        l.append(ans[i])
    for i in range(1,len(l)):
        l[i] = l[i] + l[i-1]

    plt.figure(2)
    plt.title("直线位移")
    plt.xlabel("Time")
    plt.ylabel("角度（角度制）")
    t = [time_step * i for i in range(len(l))]
    plt.plot(t, l, "*")

    #print(l)
    print(ans)


    return ans

def getpoints(x0, y0, xe, ye,step = []):
    points = []
    points.append((x0,y0))
    if xe > x0 and ye > y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        #b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x += math.cos(math.atan(k1))*i
            y += math.sin(math.atan(k1))*i
            points.append((x,y))

    if xe < x0 and ye > y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x -= math.cos(math.atan(k1)) * i
            y -= math.sin(math.atan(k1)) * i
            points.append((x, y))

    if xe < x0 and ye < y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x -= math.cos(math.atan(k1)) * i
            y -= math.sin(math.atan(k1)) * i
            points.append((x, y))

    if xe > x0 and ye < y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = x0
        y = y0
        for i in step:
            x += math.cos(math.atan(k1)) * i
            y += math.sin(math.atan(k1)) * i
            points.append((x, y))

    if ye - y0 == 0 and xe - x0 > 0 :
        x = x0
        y = y0
        k1 = 0  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        for i in step:
            x += math.cos(math.atan(k1)) * i
            y = ye
            points.append((x, y))

    if ye - y0 == 0 and xe - x0 < 0 :
        x = x0
        y = y0
        k1 = 0  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        for i in step:
            x -= math.cos(math.atan(k1)) * i
            y = ye
            points.append((x, y))

    if ye - y0 > 0 and xe - x0 == 0 :
        x = x0
        y = y0
        for i in step:
            x = xe
            y += i
            points.append((x, y))

    if ye - y0 < 0 and xe - x0 == 0 :
        x = x0
        y = y0
        for i in step:
            x = xe
            y -= i
            points.append((x, y))

    '''if (xe,ye) not in points:
        points.append((xe,ye))'''

    plt.figure(3)
    plt.title("粗插补采样点")
    plt.xlabel("X")
    plt.ylabel("Y")
    for point in points:

        plt.plot(point[0],point[1],"*")


    return points

def getheta(points = []):
    the = []
    for i in range(len(points)-1):
        Lo = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5  # 起点线段长度
        lpoint = ((points[i+1][1] - points[i][1]) ** 2 + (points[i+1][0] - points[i][0]) ** 2) ** 0.5  # 两点之间的距离
        LE = (points[i+1][0] ** 2 + points[i+1][1] ** 2) ** 0.5  # 终点线段的长度
        theta = math.degrees(math.acos((Lo ** 2 + LE ** 2 - lpoint ** 2) / (2 * Lo * LE)))  # 两线段的夹角
        the.append(theta)
    return the

def draw_omg(time_step,Theta_step,theta = []):
    tim = []
    omg = []
    jicun = []
    jicun.append(0)
    yushu = 0
    plt.figure(4)
    for i in range(len(theta)) :
        tim.append(i*time_step)
        omg.append(theta[i]/time_step)
    plt.title("角速度（连续）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    plt.plot(tim,omg, "*")
    #plt.show()
    #print(tim,omg)
    for the in theta :
        n = int((the+yushu) // Theta_step)
        yushu = the+yushu - n*Theta_step
        jicun.append(n)
    #jicun.append(0)
    #print(jicun)

    '''plt.figure(5)
    plt.title("角速度（脉冲）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    for i in range(len(jicun)-1):
        plt.plot((i * time_step,i * time_step ),(jicun[i] * Theta_step / time_step, jicun[i+1] * Theta_step / time_step), "-")
        plt.plot((i * time_step, (i+1) * time_step),(jicun[i+1] * Theta_step / time_step, jicun[i+1] * Theta_step / time_step), "-")
    plt.plot(((len(jicun)-1)*time_step,(len(jicun)-1)*time_step),(jicun[-1] * Theta_step / time_step,0))'''


    return jicun


'''#liang = valespeed(217,204,121,258,100,20,0.01)
liang = valespeed(10,20,20,10,10,20,0.01)
print(liang)
#point = getpoints(217,204,121,258,liang)
point = getpoints(10,20,20,10,liang)
print(point)
the = getheta(point)
print(the)
draw_omg(0.01,0.018,the)
plt.show()'''

