#coding=utf-8
'''
课件
'''
# import random
# star_list = [[],[],[]]
# names = ['A', 'B','C','D','E','F','G','H']
# for name in names:
#     index = random.randint(0,2)
#     star_list[index].append(name)
# for i in range(len(star_list)):
#     print('星球{}中有{}个宇航员，分别是：'.format(i, len(star_list[i])))
#     for temp in star_list[i]:
#         print(temp, '\t', end='')
#     print()


l = [x**2 for x in range(1,10) if x%2==0]
print(l)