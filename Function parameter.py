# _*_ codiong: utf-8 -*-

a = input('请输入你想计算的数字')
b = input('请输入乘方')

aint = int(a)
bint = int(b)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print('您的结果是', s)
    return s


print(power(aint))
