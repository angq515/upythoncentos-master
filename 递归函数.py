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


# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(9))
#

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        print(product)
        return product
    print(num, product)
    return fact_iter(num-1, num * product)


print(fact(5))
