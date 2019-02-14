# _*_ codiong: utf-8 -*-
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    # 我的解法：
    # L = str(n)
    # i=0
    # w = []
    # while i < (len(L)//2):
    #     if L[i] != L[len(L)-i - 1]:
    #         w.append(None)
    #         i += 1
    #     else:
    #         w.append(True)
    #         i += 1
    # if None in w:
    #     return None
    # else:
    #     return True

    # 最优解法
    return n == int(str(n)[::-1])





# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')