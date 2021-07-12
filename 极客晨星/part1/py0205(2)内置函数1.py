'''
学习str()、format()、ord()、chr()、repr()、eval()等常见的内置函数，掌握其用法
1. str(): 将字符、数值等类型转换为字符串类型
2. format():格式化输出字符串，通过{}定位
3. ord() 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
4. chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
5. repr() 函数将对象转化为供解释器读取的形式,返回一个对象的 string 格式。
6. eval() 函数用来执行一个字符串表达式，并返回表达式的值。
'''
    # 1. str()
# a = 1
# print(a,type(a))
# a = str(a)
# print(a,type(a))

    # 2. format()
# print("黄{}李{}伊".format("hello", "world"))
# print("{1}黄{0}李{1}".format("hello", "world"))
# print("{} {}李".format("hello", "world","dd"))
# print("{} {} {}".format("hello", "world"))

    # 3. ord()
# print(ord('C'))

    # 4. chr()
# print(chr(67))

    # 课堂练习
# s = '123@bc'
# print(chr(int(s[0])) + chr(int(s[1]))) #\x表示16进制，返回后面16进制数字对应的字符
#
# a = s[0]
# b = int(a)
# print(chr(b))
    # 5. repr()
# a = 's'
# print(a,type(a),len(a))
# a = repr(a)
# print(a,type(a),len(a))

    # 6. eval()
# a = eval('1')
# print(type(a))
# print(eval("2 + 3"))
# list1 = [1, 2, 3]
# str1 = 'zhangzhaoxi'
# print(str1)
# print(list1)
# print(type(list1))
# print(eval(list1))
# print(type(eval(list1)))
# eval("print('Hello Word')")
#
# hello world
# 'hello world'
#sum() #方法对序列进行求和计算
# a = sum([1,2,3,4])
# b = sum([10],20)
# print(a)

# print(int(input(1+2+3+4)))


# 张兆熙上节课的作业解答
# a = sum(int(input(1+2+3+4)))
# print(a)
# 首先input(1+2+3+4)中，计算1+2+3+4的值为10，显示在待输入界面，
# 所以会看到10，其实是提示用户输入的内容，与input("请输入数字")效果相同
# 其次int()将input结果强制转换为int型
# 最后计算sum(n),n为input输入的数，此时会报错，因为sum()方法对序列进行求和计算,而10是一个数，不是一个序列
# 正确操作：sum([1,2,3,4])；
# 上节课老师留的题没有打[],如果还有疑问可以在群里提问，或者下节课课上问老师