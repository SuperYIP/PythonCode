#coding = utf-8
# def test():
# 	print("---test---")
# def func(f):
# 	print(f)
# 	f()
# 	print("---------func-------")
#
# # t = test #t与test都指向同一地址，此时调用t和test是同样的
# func(test)

'''
装饰器特点：
1. 函数A是作为参数出现的（函数B就接收函数A作为参数-->B(A)）
2. 要有闭包的特点
'''
'''
应用方面：
不改变原函数，在原函数基础上增加新的功能
	比如淘票票网站中想要购票需先登录，则购票系统为被装饰函数，登录系统为装饰函数
'''

#定义一个装饰器
def decorate(func):
	a = 100
	def wrapper(*args, **kwargs):  #这两个参数让装饰器万能，可以传进任意参数
									#*args表示可以传进来任意个数参数，**kwargs表示可以传进任意个数关键字参数
		print('------>开始建房子')
		func(*args, **kwargs)	#此处运行house中的代码
		print('------>铺地板,a = ',a)
		print('\n')
	return wrapper

#s使用装饰器
@decorate	#装饰器函数放在被装饰函数上面
def house():
	print("我是毛坯房")
@decorate
def bighouse(size):
	print("这间房子这么大：", size)

@decorate
def whosehouse(number, name='xiaoyi'):
	print("这是%s的房子" %name)
	for i in range(number):
		print("打印number值", number)

'''
运行过程：
1. house作为被装饰函数
2. 将被装饰函数作为参数传递给装饰器decorate
3. 执行装饰器函数
'''
'''
运行结束后可以发现house地址就是wrapper地址，
	打印house地址：<function decorate.<locals>.wrapper at 0x0000021076D94828>
	可以看到地址中的wrapper字样
'''
house()		#此时调用house相当于调用wrapper
bighouse(100)
whosehouse(3, 'xiaopang')
# print(house) #打印house地址