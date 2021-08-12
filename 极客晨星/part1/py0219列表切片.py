#coding=utf-8
'''
课件
'''

# mylist = [1,2,3,4,5,6,7,8]
# print(mylist[0:4])
# print(mylist[::])
# print(mylist[0:7:2])
# print(mylist[-1:-7:-2])
# print(mylist[::-1])
# print(mylist[8:9])

# names = ['苹果', '香蕉', '哈密瓜']
# temp_list = ['牛肉', '五花肉']
# names.append(temp_list)
# print(names)
# names.extend(temp_list)
# print(names)
# print(mylist[8:20])     # 不会报错

# a = [1,2]
# b = [3,4]
# a.append(b)     # 整体追加
# print(a)
# a.extend(b)     # 逐个追加
# print(a)

fruit = ['苹果', '香蕉', '梨', '橘子']
i = 0
while i < len(fruit):
    if fruit[i] == '梨':
        fruit[i] = '苹果'
        i += 1
    else:
        i += 1
        continue
print(fruit)