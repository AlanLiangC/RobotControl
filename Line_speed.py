from PointAdd import cross_point
import math
import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
p = 0

def get_number(time_step,l_step,points):
    tim = []
    v = []
    jicun = []
    jicun.append(0)
    yushu = 0
    speed = []
    speed.append(0)
    for i in range(len(points)-1):
        x0 = points[i][0]
        y0 = points[i][1]
        xe = points[i+1][0]
        ye = points[i+1][1]
        #Address = cross_point(x0,y0,xe,ye)
        Lo = (y0 ** 2 + x0 ** 2) ** 0.5  # 起点线段长度
        LE = (ye ** 2 + xe ** 2) ** 0.5  # 终点线段的长度
        lpoint = ((ye - y0) ** 2 + (xe - x0) ** 2) ** 0.5  # 两点之间的距离
        speed.append((LE-Lo)/time_step)
        #Lmin = ((Address[0]) ** 2 + (Address[1]) ** 2) ** 0.5  # 垂线的距离
        '''if (min(xe, x0) <= Address[0] <= max(xe, x0)) and (min(ye, y0) <= Address[1] <= max(ye, y0)):
            number1 = int((abs(Lo - Lmin)+yushu) // l_step)
            yushu = abs(Lo - Lmin)+yushu-number1*l_step
            
            number2 = int((abs(LE - Lmin)-yushu) // l_step)
            number = int((abs(Lo - Lmin)) // l_step + (abs(LE - Lmin)) // l_step)
        else:'''
        number = int((abs(Lo - LE)+yushu) // l_step)
        yushu = abs(Lo - LE)+yushu-number*l_step
        if Lo - LE >= 0 :
            jicun.append(-number)
        else:
            jicun.append(number)
        #print(Lo - LE)
        #print(number)
    speed.append(0)
    plt.figure(6)
    for i in range(len(speed)):
        tim.append(i * time_step)
        v.append(speed[i] / time_step)
    plt.title("线速度（连续）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    plt.plot(tim, v, "*")

    plt.figure(7)
    plt.title("线速度（脉冲）图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    for i in range(len(jicun) - 1):
        plt.plot((i * time_step, i * time_step),
                 (jicun[i] * l_step / time_step, jicun[i + 1] * l_step / time_step), "-")
        plt.plot((i * time_step, (i + 1) * time_step),
                 (jicun[i + 1] * l_step / time_step, jicun[i + 1] * l_step / time_step), "-")
    plt.plot(((len(jicun) - 1) * time_step, (len(jicun) - 1) * time_step), (jicun[-1] * l_step / time_step, 0))

    #plt.show()
    return jicun



    #print(jicun)
#points = [(20, 20), (19.95, 19.995), (19.8, 19.98), (19.55, 19.955000000000002), (19.2, 19.92), (18.75, 19.875), (18.2, 19.82), (17.55, 19.755), (16.8, 19.68), (15.950000000000001, 19.595), (15.000000000000002, 19.5), (14.000000000000002, 19.4), (13.000000000000002, 19.299999999999997), (12.000000000000002, 19.199999999999996), (11.000000000000002, 19.099999999999994), (10.000000000000002, 18.999999999999993), (9.000000000000002, 18.89999999999999), (8.000000000000002, 18.79999999999999), (7.000000000000002, 18.69999999999999), (6.000000000000002, 18.599999999999987), (5.000000000000002, 18.499999999999986), (4.000000000000002, 18.399999999999984), (3.0000000000000018, 18.299999999999983), (2.0000000000000018, 18.19999999999998), (1.0000000000000018, 18.09999999999998), (1.887379141862766e-15, 17.99999999999998), (-0.999999999999998, 17.899999999999977), (-1.9999999999999978, 17.799999999999976), (-2.999999999999998, 17.699999999999974), (-3.999999999999998, 17.599999999999973), (-4.999999999999997, 17.49999999999997), (-5.999999999999997, 17.39999999999997), (-6.999999999999997, 17.29999999999997), (-7.999999999999997, 17.199999999999967), (-8.999999999999996, 17.099999999999966), (-9.999999999999996, 16.999999999999964), (-10.999999999999996, 16.899999999999963), (-11.999999999999996, 16.79999999999996), (-12.999999999999996, 16.69999999999996), (-13.999999999999996, 16.59999999999996), (-14.999999999999996, 16.499999999999957), (-15.949999999999996, 16.40499999999996), (-16.799999999999997, 16.319999999999958), (-17.549999999999997, 16.24499999999996), (-18.199999999999996, 16.179999999999957), (-18.749999999999996, 16.124999999999957), (-19.199999999999996, 16.079999999999956), (-19.549999999999997, 16.044999999999956), (-19.799999999999997, 16.019999999999957), (-19.949999999999996, 16.004999999999956), (-19.999999999999996, 15.999999999999956)]
#get_number(0.1,0.01,points)
