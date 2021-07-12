# coding=utf-8
'''

range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表，遍历时左闭右开
'''

# a = range(5)
# print(a)    # range(0, 5)
# print(type(a))  # <class 'range'>

# for i in range(10,1,-3):
#     print(i)

# str1 = 'python'
# for i in str1:
#     print(i)
#     if i == 't':
#         print('hello world')

# str1 = 'hello python'
# for temp in range(len(str1)):
#     print(temp, '\t', str1[temp])

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}*{}={}'.format(j, i, j * i), '\t', end='')
#     print()


# str1 = 'hello python'
# for temp in range(len(str1)):
#     print(temp, '\t', str1[temp])

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}*{}={}'.format(j ,i, i*j), '\t',end='')
#     print()
