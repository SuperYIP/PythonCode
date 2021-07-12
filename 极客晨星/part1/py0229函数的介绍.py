# coding=utf-8
'''
课件
'''


# def yihaidi():
#     print('我是伊海迪')
#     print('今天22岁')
#
# for i in range(20):
#     print('当前是第%d次执行:' % (i+1))
#     yihaidi()


def sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

result = sum(10)
print(result)



