import numpy as np
import math
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
    omg = theta / (n * time_step)
    for i in range(1, N + 1):
        step = eval("%.6f"%((omg * i ** 2 * time_step - omg * (i - 1) ** 2 * time_step) / (2 * N)))
        jiasu = np.append(jiasu,step)
    cishu = n - N
    print(cishu)
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
    #plt.show()
    print(jiasu)
    print("/**********************************/")
    print(yunsu)
    print("/**********************************/")
    print(jiansu)
    print("/**********************************/")
    print(ans)
    return ans


cirspeed(100,150,150,100,v0, num, time_step,-50,[10,10])
#get_circle(100,150,150,100,-50,0)