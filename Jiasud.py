import numpy as np
import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
def valespeed(x0,y0,xe,ye,v0,a,time_step):

    lz=((xe-x0)**2+(ye-y0)**2)**0.5;
    ll=0   #路程
    #a=1;     #加速度
    v=0     #初始速度

    lll=[]
    while v<v0:

        l=v*time_step+0.5*a*time_step**2
        v=v+a*time_step
        ll=ll+l
        lll.append(l)
        l1=ll
    l3=lz-l1
    while ll<l3:

        l=v*time_step
        ll=ll+l
        lll.append(l);


    while v>=0:

        l=v*time_step-0.5*a*time_step
        v=v-a*time_step
        ll=ll+l
        lll.append(l)
    print(len(lll))

    x = []
    y = []
    for i in range(len(lll)):
        x.append((2**0.5/2)*lll[i])
        y.append((2**0.5/2)*lll[i])

    x[0] = x[0] + 1
    y[0] = y[0] + 2
    for i in range(1,len(x)):
        x[i] = x[i] + x[i-1]
        y[i] = y[i] + y[i-1]

    point = []


    fig = plt.figure()  # 创建一个没有 axes 的 figure
    plt.title("角速度图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")
    l = [i for i in range(len(lll))]
    plt.plot([0,1.4,1.4,6,6,7.4],[1.323,1.323,0,0,-1.323,-1.323], "-")

    plt.show()


valespeed(1,2,10,11,2,1,0.1)
