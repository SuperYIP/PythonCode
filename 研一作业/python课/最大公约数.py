# coding=utf-8
a = eval(input("输入第一个数字"))  #input返回一个字符串，eval将其转换为数字，int也能做到
b = eval(input("输入第二个数字"))
c = a * b
if a < b:   #保证a>b
    a, b = b, a

while a % b != 0:   #辗转相除法
    a, b = b, a % b
print('最大公约数:', b)
print('最小公倍数:', int(c / b))
