# coding=utf-8
'''
1. filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
    该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
2. map()    接收一个函数f和一个可迭代对象，并通过把函数f依次作用在可迭代对象的每个元素上，得到一个新的可迭代对象并返回。
3. reduce() 对参数序列中元素进行累积
    首先把前两个元素传给函数参数，函数加工后，然后把得到的结果和第三个元素作为两个参数传给函数参数，
    函数加工后得到的结果又和第四个元素作为两个参数传给函数参数，依次类推。如果传入了 initial 值，
    那么首先传的就是 initial值和第一个元素。经过这样的累计计算之后合并序列到一个单一返回值

'''

# 1
# def is_odd(n):
#     return n % 2 == 1
# list1 = list(range(1,11))
# print(list(filter(is_odd, list1)))

# 2
# def f(x):
#     return x * x
# list1 = list(range(1,11))
# print(list(map(f, list1)))

# 3
# from functools import reduce
# def add(x, y):
#     return x + y
#
# res = reduce(add, [1,2,3,4,5])
# print(res)

# 课堂练习
# from functools import reduce
# sentences = ['The Deep Learning textbook is a resource intended to help students and '
#              'practitioners enter the field of machine learning in general and deep '
#              'learning in particular. ']
# word_count = sentences[0].count('learning')
# print(word_count)
# word_count2 = reduce(lambda a,x: a+x.count("learning"),sentences,0)
# # 此时reduce第三个参数initial赋值为0，将0和sentencs列表的第一个元素传递给匿名函数，故a=0,x=sentences[0]
# print(word_count2)