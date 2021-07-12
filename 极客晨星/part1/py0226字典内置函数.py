# coding=utf-8

'''
内置函数：
1. len(): 计算字典元素个数，即键的总数
2. get(): 返回指定键的值，如没有则返回默认值，默认值不指定则为None
3. keys(): 以列表返回所有键
4. values(): 以列表返回所有值
5. items(): 返回元组数组
6. popitem(): 返回并删除字典中的最后一对键和值
7. update(): dict.update(dict1),把dict1的键值对更新到dict中
8. clear(): 删除字典内所有元素 dict={}
del dict
'''
    # 字典键不可重复
# dict = {'a':1, 'b':2, 'b':3, 2:55}
# print(dict['b'])
# print(dict)

    # 字典键需为不可变类型，如字符串，数字，元组
# dict1 = {'abc':123, 98.6:37, (1,2):"小明"}
# print(dict1['abc'],dict1[(1,2)],dict1[98.6])
# dict2 = {[1,2]:123}

    # 1. len()
# print(len(dict))

    # 2. get()
# print(dict[7])
# print(dict.get(7, 'ss'))

    # 3. keys()
# dict = {'a':1, 'b':3, 2:55}
# print(dict.keys())
# for temp in dict.keys():
#     print(temp)

# print(dict.keys()[1])   # 不可索引访问，可以遍历

    # 4. values()
# dict = {'a':1, 'b':3, 2:55}
# print(dict.values())

    # 5. items()
# dict = {'a':1, 'b':3, 2:55}
# print(dict.items())

    # 6. popitem()
# dict = {'a':1, 'b':3, 2:55}
# print(dict)
# print(dict.popitem())
# print(dict)

    # 7. update()
# dict = {'a':1, 'b':3, 2:55}
# dict1 = {'ww': 'ss', 4:'zhu'}
# dict.update(dict1)
# print(dict)

    # 8. clear()
# dict1 = {'a':1, 'b':3, 2:55}
# print(dict)
# dict.clear()
# print(dict)
# del dict1
# print(dict1)


# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
# print (dict.keys())
# print(dict.values())
# # 遍历字典列表
# for key in dict.items():
#     print(key[1])
