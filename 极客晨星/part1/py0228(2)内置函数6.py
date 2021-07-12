# coding=utf-8
'''
1. frozenset:返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
            用法：frozenset([iterable])：iterable -- 可迭代的对象，比如列表、字典、元组等等
2. zip:函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。节约内存
'''
# 1. frozenset
# a = frozenset()
# print(a, '\t', type(a))
# b = frozenset(range(5))
# print(b, '\t', type(b))
# s = frozenset('hello')
# print(s, '\t', type(s))     # 集合三个性质：明确性，无序性，互异性
# l = frozenset([1,2,3,4])
# print(l, '\t', type(l), '\t', len(l))

# 2.zip
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# temp1 = zip(a)
# print(temp1, '\t', type(temp1))
# temp2 = zip(a,b)
# print(temp2, '\t', type(temp2))
# print(list(temp1))
# print(list(temp2))
# temp3 = zip(a,b,c)
# temp3_list = list(temp3)
# print(temp3_list, '\t', type(temp3_list), '\t', len(temp3_list))
# print(temp3_list[0][0])
#
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# temp = zip(a,b,c)
# # print(temp,type(temp))
# # print(list(temp))
# x, y, z = zip(*temp)
# print(x,y,z)

# 课堂练习
# tb = [['小明', '小红', '小白'], [90, 80, 70]]
# # # tb = (('小明', '小红', '小白'), (90, 80, 70))
# a, b, c = zip(*tb)
# print(a, b, c)
# score = dict(zip(*tb))
# print(score)
# print(list(zip(*tb)))

# 课堂练习
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dic = dict(zip(keys, values))
# print(keys)
# print(values)
# print(dic)
# print(list(zip(keys, values)))
