# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

# -*- coding: utf-8 -*-


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        m = L[0]
        n = L[0]

        for a in L:
            if m <= a:
                m = a
            if n > a:
                n = a

        return (n, m)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
if findMinAndMax([7]) != (7, 7):
    print('测试失败!2', findMinAndMax([7]))
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3', findMinAndMax([1,7]))
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4', findMinAndMax([7,1,3,9,5]))
else:
    print('测试成功!')