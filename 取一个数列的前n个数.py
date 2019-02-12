# _*_ codiong: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# def pickn(n, W=[]):
#     number = 0
#     p = []
#     if n > len(W):
#         return print(n, 'is biggher than the list lenth, the lenth of the list is', len(W))
#     else:
#         while number < n:
#             p.append(W[number])
#             number += 1
#         return p
#
#
# print(pickn(3, ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']))

r = []
n = 4
for i in range(n):
    r.append(L[i])
print(L)
print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:-1])

