#coding=utf-8
'''
课件
'''

# def rescursion(num):
#     if num > 1:
#         return num * rescursion(num-1)
#     else:
#         return 1
# a = rescursion(3)
# print(a)

# def power(n, m):
#     if m == 1:
#         return n
#     else:
#         return power(n,m-1) * n
# result = power(2,3)
# print(result)

# sum = lambda num1, num2: num1 + num2
# print(sum(1,2))

# stus = [
#     {"name": "zhangsan", "age": 18},
#     {"name": "lisi", "age": 19},
#     {"name": "wangwu", "age": 17}
# ]
# stus.sort(key=lambda x:x['name'])
# # 当待排序列表的元素由多字段构成时，我们可以通过sorted(iterable，key，reverse)的参数key来制定我们根据那个字段对列表元素进行排序。key=lambda 元素: 元素[字段索引]
# # key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# print(stus)

func = lambda x, y: x/y if x>y else x*y
print(func(2,3))