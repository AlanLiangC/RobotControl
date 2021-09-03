import math
from PointAdd import cross_point
def distance(angle,x0,y0,xe,ye):  # 计算交点函数
    if xe-x0 == 0:
        x = xe
    else:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        if angle%90 == 0 and angle != 0:  # L2直线斜率不存在操作
            k2 = None
            b2 = 0
        else:
            k2 = math.tan(math.radians(angle))  # 斜率存在操作
            b2 = 0
        if k2 == None:
            x = 0
        else:
            x = (b2 - b1) * 1.0 / (k1 - k2)
        y = k1 * x * 1.0 + b1 * 1.0
    return x


def find_point(theta0,step,sn,theta,x0,y0,xe,ye):
    pmin = cross_point(x0,y0,xe,ye)
    x_add = []
    number = int(theta // step)
    add = 0
    if sn == 0 :            #逆时针
        for i in range(number):
            x_add.append(distance(theta0,x0,y0,xe,ye))
            theta0 += step
        for i in range(number-1):
            if (x_add[i] <= pmin[0] <= x_add[i+1]) or (x_add[i] >= pmin[0] >= x_add[i+1]) :
                add = i+1
                break
    elif sn == 1 :
        for i in range(number):
            x_add.append(distance(theta0,x0,y0,xe,ye))
            theta0 -= step
        for i in range(number-1):
            if (x_add[i] <= pmin[0] <= x_add[i+1]) or (x_add[i] >= pmin[0] >= x_add[i+1]) :
                add = i+1
                break
    return add
#print(find_point(45,1,0,90,5,5,-5,5))


