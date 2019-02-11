# # -*- coding: utf-8 -*-
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(my_abs('a'))


# 本程序是一个一元二次方程的解法：ax*x + bx + c = 0
# 解法方程为:https://zh.wikipedia.org/wiki/%E4%B8%80%E5%85%83%E4%BA%8C%E6%AC%A1%E6%96%B9%E7%A8%8B

import math


def quadratic(a, b, c):
    s = b*b - 4*a*c
    if s >= 0:
        jieguo1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        jieguo2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return jieguo1, jieguo2
    else:
        jieguo1 = (-b - math.sqrt(-(b*b - 4*a*c)))/(2*a)
        jieguo2 = (-b + math.sqrt(b * b - 4*a*c)) / (2*a)
        return jieguo1, jieguo2


print('quadratic(2,3,1) =', quadratic(2, 3, 1))
print('quadratic(1,3,-4) =', quadratic(1, 3, -4))


if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
