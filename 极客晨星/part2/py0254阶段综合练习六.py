#coding=utf-8
'''


'''

# 1.
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(6))

# 2
# def is_palindrom(s):
#     if len(s) < 2:
#         return '是回文字符串'
#     if s[0] == s[-1]:
#         return is_palindrom(s[1:-1])
#     else:
#         return '不是回文字符串'
# print(is_palindrom('ababa'))

# 3
# square_list = list(map(lambda x: x*x,[x for x in range(1, 101)]))
# print(square_list)

# 4
# def func(listinfo):
#     return list(filter(lambda x: x<100 and x%2==0, listinfo))
#
# listinfo = [133,88,24,33,232,44,11,44]
# print(func(listinfo))

# 