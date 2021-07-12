#coding=utf-8
'''
课件
'''

# a, b = {'a':11, 'b':12}
# print(a, '\n', b, sep='')   # sep表示两个字符间的间隔符号,默认为空格,此时为空

a = [1,2]
b = a
c = a[:]
a.append(3)
print(a,id(a))
print(b,id(b))
print(c,id(c))
# https://zhuanlan.zhihu.com/p/161374254