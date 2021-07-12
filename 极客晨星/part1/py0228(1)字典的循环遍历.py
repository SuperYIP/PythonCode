#coding=utf-8
'''
课件
'''

chars = ['a', 'b', 'c', 'd']

for i, temp in enumerate(chars):
    print('%d,%s' % (i, temp))


dict1 = {'name': '小明', 'age': 18}

for index, item in enumerate(dict1.items()):
    print(index, item)

