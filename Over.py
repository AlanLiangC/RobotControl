# -*- coding:utf-8 -*-
import math
from Findmin import find_point
from Distance import distance
from Val_speed import *
from JZB import *
from Line_speed import get_number

Theta_step = 0.01          #转角脉冲当量
L_step = 0.002               #伸缩脉冲当量
time_step = 0.02             #粗插补采样周期
num = 5                    #加速次数
v0 = 20                     #匀速
sn = 0          #判断逆时针顺时针 0为逆时针 1为顺时针
way = 0
T = 0
rout = []


def judge_quadrant(x0, y0, xe, ye):
    if (x0 == 0 and y0 == 0) or (xe == 0 and ye == 0) or (y0/x0 == ye/xe):
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

def get_whole(x0, y0, xe, ye):
    ans = valespeed(x0,y0,xe,ye,v0,num,time_step)
    sn = judge_quadrant(x0, y0, xe, ye)
    points =  getpoints(x0,y0,xe,ye,ans)
    print(points)
    if sn == 2:
        ao = []
        l = get_number(time_step, L_step, points)
        for i in range(len(l)):
            ao.append(0)
    else:
        the = getheta(points)
        ao = draw_omg(time_step,Theta_step,the)
        l = get_number(time_step, L_step, points)

        if (sn) :
            for i in range(len(ao)):
                ao[i] = -ao[i]

    y = ao + l
    p = 0
    for i in range(len(l)):
        p += l[i]
    print(y)
    return y,points



valespeed(0,100,100,0,v0,num,time_step)
#get_whole(100,100,0,0)


