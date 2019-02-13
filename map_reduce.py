# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：

# _*_ codiong: utf-8 -*-
from functools import reduce

Smallword = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
             'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
             'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}

Bigword = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
           'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
           'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

def small(x, y):
    if x in Smallword.keys():
        x = Smallword[x]
    else:
        x = x
    if y in Smallword.keys():
        y = Smallword[y]
    else:
        y = y
    return x + y


def allsmall(x):
    return reduce(small, x)


def firstletter(x):
    if x in Bigword.values():
       x = x
    else:
        x = Bigword[x]
    return x


def normalize(name):
    firstname = name[0]
    restname = name[1:]
    return(firstletter(firstname)+allsmall(restname))



# 测试:
L1 = ['adam', 'LISA', 'barT','AFjqwSDGFjl','aaDD']
L2 = list(map(normalize, L1))
print(L2)