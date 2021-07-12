#coding=utf-8
'''
课件
'''

# 1 去除列表中重复数据
# list1 = ['b', 'c', 'd', 'c', 'b', 'a', 'a']
# set1 = set(list1)   # 集合中不允许数据重复
# print(set1)
#
# list2 = []
# for temp in list1:
#     if temp not in list2:
#         list2.append(temp)
# print(list2)

# 2
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic1 = {}
# li_more = []
# li_less = []
# for temp in li:
#     if temp == 66:
#         continue
#     elif temp > 66:
#         li_more.append(temp)
#     else:
#         li_less.append(temp)
# dic1['k1'] = li_more
# dic1['k2'] = li_less
# print(dic1)

# # 3
# f = open(r'C:\Users\伊海迪\Desktop\1.txt', 'w', encoding='utf-8')
# s = input('请输入一个字符串：')
# s = s.upper()
# f.write(s)

# # 4
# def checkList(list1):
#     if len(list1) > 2:
#         return list1[0:2]
#     else:
#         return list1
#
# l = [11, 22,44]
# result = checkList(l)
# print(result)