#coding=utf-8
'''
课件
'''

# def calculateNum(num):
#     result = 0
#     for i in range(1, num+1):
#         result += i
#     return result
#
# print(calculateNum(50))

# def testB():
#     print('----testB start----')
#     print('此时执行testB')
#     print('----testB end----')
# def testA():
#     print('----testA start----')
#     testB()
#     print('----testA end----')
# testA()

def huahengxian():
    print('-' * 30)

def huahengxian_n(num):
    for i in range(num):
        huahengxian()

huahengxian_n(3)