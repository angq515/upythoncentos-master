# -*- coding: utf-8 -*-

# 请编写hanoi(n, a, b, c)函数，它接收参数n，
# 表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法，例如：

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(5, 'A', 'B', 'C')


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# move(3, 'A', 'B', 'C')