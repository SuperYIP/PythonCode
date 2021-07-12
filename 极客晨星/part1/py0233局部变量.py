#coding=utf-8
'''
课件
'''
# a = 100
#
# def test1():
#     global a
#     print(a)
#     a = 200     # python的函数中和全局同名的变量，如果你有修改变量的值就会变成局部变量，
#                 # 对该变量的引用就会出现没定义这样的错误了。 可以使用global声明变量未全局变量
# def test2():
#     print(a)
# test1()
# test2()

# def test1():
#     a = 300
#
# def test2():
#     print(a)
#     a = 400
#     print('test2中的a的值：{}'.format(a))
# test1()
# test2()

a = 100
b = 200

def test1():
    global a,b
    print('修改前a的值{}'.format(a))
    a = 200
    print('修改后a的值{}'.format(a))

def test2():
    print(a)

test1()
test2()