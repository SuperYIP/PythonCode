#coding = utf-8
'''
带参数的装饰器是三层的
最外层的函数负责接收装饰器参数
里面的内容还是原来装饰器的内容
'''

def outer(a):	#第一层
	def decorate(func):		#第二层
		def wrapper(*args, **kwargs):	#第三层
			func(*args)
			print("--->铺地砖{}快".format(a))
			print('\n')
		return wrapper
	return decorate

@outer(10)
def house(time):
	print("时间{}，是毛坯房".format(time))

@outer(100)
def street():
	print("新修的路")

house('2020-03-14')
street()

'''
除此之外，被装饰函数可以有多个装饰器，按照调用时离被装饰函数的远近先后调用
例如：
@decorate1
@decorate2
def house():
	....
此时先调用decorate2
'''