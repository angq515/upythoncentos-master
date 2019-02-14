# _*_ codiong: utf-8 -*-

lambda语法，，调用的参数是':'前面的值，返回的值是一':'后面定义的函数。
而调用的参数是通过被定义的函数的上一级

def count():
    def f():
        return lambda j: j*j
    fs = []
    for i in range (1, 4):
        fs.append(f())
    return fs
