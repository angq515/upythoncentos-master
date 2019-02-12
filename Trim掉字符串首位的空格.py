# # _*_ codiong: utf-8 -*-

# def trim(s):
#     end = len(s) - 1
#     start = 0
#     if end >= 0:
#         while s[start] == ' ':
#             if start < end:
#                 start = start + 1
#             else:
#                 s = ''
#                 return s
#         while s[end] == ' ':
#                 end -= 1
#         s = s[start:end+1]
#         return s
#     else:
#         return s

# 递归写法

def trim(s):
    if s[:1] == ' ':
        s = s[1:]
        return trim(s)
    if s[-1:] == ' ':
        s = s[:-1]
        return trim(s)
    else:
        return s



# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!', trim('    '))