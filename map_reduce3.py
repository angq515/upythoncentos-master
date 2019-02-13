# -*- coding: utf-8 -*-
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce

# def str2float(s):
#
#     number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#     def digits(x):
#         i = 0
#         while i <= len(x)-1:
#             if x[i] == '.':
#                 return len(x)-i-1
#             else:
#                 i += 1
#         return 0
#
#
#     def checknum(x):
#         if x in number.keys():
#             return number[x]
#         pass
#
#
#     def fun(x, y):
#         if y == None:
#             return x
#         else:
#             return 10*x+y
#
#     return reduce(fun, map(checknum, s))/(10**digits(s))


# 下面是别人的最优解法
def str2float(s):
    m = len(s) - s.index('.') - 1
    def char2num(s):
        digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9, '.':None}
        return digits[s]

    def fn(x,y):
        if y == None:
            return x
        else:
            return x*10 + y

    return reduce(fn, map(char2num, s))/(10**m)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')