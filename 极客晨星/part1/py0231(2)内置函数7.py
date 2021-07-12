# coding=utf-8
'''
1. all:用于判断给定的可迭代参数 iterable 中的所有元素是否全部为 TRUE，如果是返回 True，否则返回 False。全ture才true
2. any:用于判断给定的可迭代参数 iterable 中的所有元素是否全部为 False，如果是返回 False，否则返回 True。有ture则true
all()全部为True，返回True，否则返回False
any()只要有一个True，就返回True，否则返回False
'''

# score = [89, 78, 100, 67, 0, 45]
# if all(score):
#     print('没有无效的成绩')
# else:
#     print('有无效成绩')
#     for temp in score:
#         if temp:
#             pass
#         else:
#             print('无效成绩是:{}'.format(temp))
#             score.remove(temp)
# print('处理后的成绩列表是：',score)





# print(all(score))


# a = [1,2,3]
# b = [1,2,3,[]]
# c = [1,2,3,None]
# d = [1,2,3,0]
# e = [1,2,3,'']
# f = [1,2,3,False]
# print(all(a))
# print(all(b))
# print(all(c))
# print(all(d))
# print(all(e))
# print(all(f))
