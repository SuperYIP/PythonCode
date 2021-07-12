#coding=utf-8
## 复习
'''
元组与列表类似。简单复习列表知识。
    列表引出：
    在前面的学习中，我们知道字符串可以存储一串信息。比如，存储一个名字：name="灰太狼"
    那么问题来了，如果想要把喜洋洋与灰太狼动画片的所有名字都存储起来该怎么做呢？
    1. 定义10个，20个，100个变量
    name1="喜羊羊" name2="灰太狼" name3="红太狼" ……
    2. 使用列表
    names=["喜羊羊" ,"慢羊羊" ,"美羊羊" ,"灰太狼"]
    在python中，用方括号[]来表示列表，并且用逗号来分割其中的元素。names=["喜羊羊" ,"慢羊羊" ,"美羊羊" ,"灰太狼"]
    列表是有序集合，因此要访问列表的任何元素，只需要通过元素的位置或索引即可。
    要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。print(names[0])
'''

# name = "灰太狼"
# # 方式1，定义很多个变量
# name1 = "喜羊羊"; name2 = "灰太狼"; name3 = "红太狼"
# # 方式2，定义一个列表，每个列表元素是一个名字
# names = ["喜羊羊", "慢羊羊", "美羊羊", "灰太狼"]
# # 获取列表元素
# print(names[0])
# print(names[1])
# # 遍历列表所有元素
# for name in names:
# 	print(name)
# for name in names:
#     print(name)
# # 修改列表元素
# names[0] = "伊老师"
# print(names)

## 元组
# # 只包含一个元素，不加逗号变为int型
# tup_t = (5,)
# print(type(tup_t))
# tup_r = (5)
# print(type(tup_r))
#
# 访问元组
# tup = (1,2,3,4,5,6)
# print(tup[0])
#
# 修改元组
# tup = (1,2,3,4,5,6)
# tup[2] = 10

# 连接元组
# tup1 = (1,2,3,4,5,6)
# tup2 = (7,8,9)
# tup3 = tup1 + tup2
# print(tup3)
# tup1 = (1,2,3,4,5,6)
# tup2 = (7,8,9)
# tup3 = tup1 + tup2
# print(tup3)

# 删除元组
# del tup3[0] # 元组不允许删除单个元素
# del tup3    # 可以删除整个元组
# print(tup3)

# 元组其他操作
#     #计算元组个数
# tup = (1,2,3)
# print(len(tup))
    #复制
# tup = ('HI',)
# tup = ('HI',)
# tup = tup * 4
# print(tup)
    #元素是否存在
# print(3 in (1,2,3))
# tup = (1,2,3)
# print(4 in tup)
    #迭代

# tup = (1,2,3)
# for i in tup:
#     print(i)
# for x in (1,2,3):
#     print(x)

# # 元组索引、截取
# tup = (1,2,3,4,5,6)
# print(tup[2])
# print(tup[2:5])
# tup = (1,2,3,4,5,6)
# print(tup[1:5])

# 将列表转换为元组：tuple(list)
# list = [1,2,3,4,5,6]
# print(type(list))
# print(type(tuple(list)))
# list = [1,2,3,4,5,6]
# print(type(list))
# print(type(tuple(list)))
# 课堂练习
# tu = ('alex', 'eric', 'Witharush')
# print("第一题：", len(tu))
# print("第二题：", tu[1])
# print("第三题", tu[1:3])
# print("第四题：")
# for i in tu:
#     print(i)
# print("第五题：")
# for j in range(len(tu)):  # for j in [0,1,2]:
#     print(j)


# 课后作业
# li = []
# for i in range(1, 9):
#     j = i
#     for j in range(1, 9):
#         if i != j:
#             li.append("".join([str(i), str(j)]))
# print(li)
# print(len(li))
