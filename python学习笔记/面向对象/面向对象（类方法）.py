#coding=utf-8

#讲解类方法
'''
特点：
1. 定义需要依赖装饰器@classmethod
2. 类方法中参数不是一个对象，而是一个类
3. 类方法中只能使用类属性
4. 类方法中不可以使用普通方法

类方法作用：
1. 因为只能访问类属性和类方法，可以完成对象创建之前的动作
'''
class Dog():
	test = '测试类方法'
	def __init__(self, nickname):	#传进来的是对象
		self.nickname = nickname

	def run(self):
		print('{}在院子里跑来跑去！'.format(self.nickname))
	@classmethod
	def test(cls):	#类方法 ，传进来的是类
		print(cls)
Dog.test()	#在此之前还未创建对象，同样可以调用类方法（-->类方法不依赖于对象）
dog1 = Dog('大黄')
dog1.run()
dog1.test()