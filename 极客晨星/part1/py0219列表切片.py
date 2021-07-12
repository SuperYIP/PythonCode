#coding=utf-8
'''
课件
'''

# mylist = [1,2,3,4,5,6,7,8]
# print(mylist[8:20])     # 不会报错

a = [1,2]
b = [3,4]
a.append(b)     # 整体追加
print(a)
a.extend(b)     # 逐个追加
print(a)