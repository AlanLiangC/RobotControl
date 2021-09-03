import math
import time
import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
def getpoints(step,x0, y0, xe, ye):
    points = []
    points.append((x0,y0))
    if xe > x0 and ye > y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        #b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = math.cos(math.atan(k1))*step+x0
        y = math.sin(math.atan(k1))*step+y0
        while x <= xe and y <= ye:
            points.append((x,y))
            x += math.cos(math.atan(k1)) * step
            y += math.sin(math.atan(k1)) * step

    if xe < x0 and ye > y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        #b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = -abs(math.cos(math.atan(k1))*step)+x0
        y = abs(math.sin(math.atan(k1))*step)+y0
        while x >= xe and y <= ye:
            points.append((x,y))
            x -= abs(math.cos(math.atan(k1))) * step
            y += abs(math.sin(math.atan(k1))) * step

    if xe < x0 and ye < y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        #b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = -abs(math.cos(math.atan(k1))*step)+x0
        y = -abs(math.sin(math.atan(k1))*step)+y0
        while x >= xe and y >= ye:
            points.append((x,y))
            x -= abs(math.cos(math.atan(k1))) * step
            y -= abs(math.sin(math.atan(k1))) * step

    if xe > x0 and ye < y0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        #b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = abs(math.cos(math.atan(k1))*step)+x0
        y = -abs(math.sin(math.atan(k1))*step)+y0
        while x <= xe and y >= ye:
            points.append((x,y))
            x += abs(math.cos(math.atan(k1))) * step
            y -= abs(math.sin(math.atan(k1))) * step

    if ye - y0 == 0 and xe - x0 > 0 :
        k1 = 0  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = abs(math.cos(math.atan(k1)) * step) + x0
        y = ye
        while x <= xe :
            points.append((x, y))
            x += abs(math.cos(math.atan(k1))) * step

    if ye - y0 == 0 and xe - x0 < 0 :
        k1 = 0  # 计算k1,由于点均为整数，需要进行浮点数转化
        # b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        x = -abs(math.cos(math.atan(k1)) * step) + x0
        y = ye
        while x >= xe :
            points.append((x, y))
            x -= abs(math.cos(math.atan(k1))) * step

    if ye - y0 > 0 and xe - x0 == 0 :
        x = xe
        y = y0 + step
        while y <= ye :
            points.append((x, y))
            y += step

    if ye - y0 < 0 and xe - x0 == 0 :
        x = xe
        y = y0 - step
        while y >= ye :
            points.append((x, y))
            y -= step


    '''if (xe,ye) not in points:
        points.append((xe,ye))'''

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

def draw_omg(time_step,theta = []):
    tim = []
    omg = []
    plt.figure(1)  # 创建一个没有 axes 的 figure
    for i in range(len(theta)) :
        tim.append(i*time_step)
        omg.append(theta[i]/time_step)
    plt.title("角速度图像")
    plt.xlabel("时间")
    plt.ylabel("角速度")

    plt.plot(tim,omg, "-")
    plt.show()


'''points = getpoints(0.5,20,-5,-10,20)
print(points)
the = getheta(points)
print(the)
draw_omg(0.05,the)'''

