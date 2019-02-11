# _*_ codiong: utf-8 -*-

#
# def enroll(name, gender, city = 'Beijing', age = 6):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#     return ' '
#
#
# print(enroll('stephen', 'male', age=30))

def add_end(L=[])
    L.append('End')
    return  L
# 这个参数的默认参数会不断变化，需要按照下列方式进行定义

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L