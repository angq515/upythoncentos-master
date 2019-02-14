# _*_ codiong: utf-8 -*-

# 假设我们用一组tuple表示学生名字和成绩：
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

L = [('Quan',100), ('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     return t[0]
#
#
# # 再按成绩从高到低排序：
# def by_score(t):
#     return t[1]
#
#
#
# L2 = sorted(L, key=by_name)
# print(L2)
#
# L2 = sorted(L, key=by_score, reverse=True)
# print(L2)
#

# 简便解法


def by_name(t):
    return sorted(t, key=lambda t: t[0])
print(by_name(L))

def by_score(t):
    return sorted(t, key=lambda t: t[1], reverse=True)
print(by_score(L))