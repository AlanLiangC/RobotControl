def cross_point(x0,y0,xe,ye):  # 计算交点函数
    if xe-x0 != 0:
        k1 = (ye - y0) * 1.0 / (xe - x0)  # 计算k1,由于点均为整数，需要进行浮点数转化
        b1 = y0 * 1.0 - x0 * k1 * 1.0  # 整型转浮点型是关键
        if k1 == 0:  # L2直线斜率不存在操作
            k2 = None
            b2 = 0
        else:
            k2 = -1/k1  # 斜率存在操作
            b2 = 0
        if k2 == None:
            x = 0
        else:
            x = (b2 - b1) * 1.0 / (k1 - k2)
        y = k1 * x * 1.0 + b1 * 1.0
    else:
        x = xe
        y = 0
    return [x, y]
