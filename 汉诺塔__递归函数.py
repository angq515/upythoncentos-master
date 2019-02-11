# _*_ codiong: utf-8 -*-

# n! = 1*2*3*...*n
# 我的方法：
# def fact(n):
#     x = 1
#     i = n
#     while i > 0:
#         x = x*(n-i+1)
#         i -= 1
#     return x
#
# print(fact(5))


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(999))