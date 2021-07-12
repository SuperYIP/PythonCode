#coding=utf-8
'''
1. 错误
2. ('h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n')
3. [{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}]
4. 报错
5. {}
6. name
   age
7. 错误
'''
# 1
# tu = ('alex','eric','rain')
# tu[1] = 'lock'
# 元组索引要用[]，tu[1] == 'lock'可以，tu[1] = 'lock'不可以

# 2
# str = "hello python"
# tup1 = tuple(list(str))
# print(tup1)

# 3
# a = [{i:j} for i,j in enumerate(range(5))]
# print(a)
# print(type(a))
# print(type(a[1]))
# print(list(range(1,5)))
# <class 'list'>
# <class 'dict'>
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

# 4
# info = {'name':'班长', "id":100, 'sex':'f', 'address':'中国北京'}
# del info
# print(info)

# del:删除变量
    # 扩展
# a = 1  # 对象1 被变量a引用，对象1的引用计数器为1
# b = a  # 对象1 被变量b引用，对象1的引用计数器加1
# c = a  # 1对象1 被变量c引用，对象1的引用计数器加1
# del a  # 删除变量a，解除a对1的引用
# del b  # 删除变量b，解除b对1的引用
# print(c)  # 最终变量c仍然引用1

# 5
# dict1 = {'Name': '小明', 'Age': 7, 'Class': 'First'}
# dict1.clear()
# print(dict1)
# dict1.clear():清空字典

# 6
# dic = {"name": "小明", "age": 18}
# print(dic.keys())
# print(dic.values())
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)
#
# for key,value in zip(dic.keys(), dic.values()):
#     print(key, value)

# 7
# tup1 = (1)
# print(type(tup1))
# tup2 = (1,)
# print(type(tup2))

# print(list(range(0,10,-1)))