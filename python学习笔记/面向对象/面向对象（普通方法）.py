#coding=utf-8

#所有的类名要求首字母大学，多个单词使用驼峰式命名
'''
class 类名：
	属性： 特征

	方法： 动作
		普通方法，
		类方法，
		静态方法，
		魔术方法：__名字__()
'''
#定义类
class Cat:
	type = '猫' #类属性
	def __init__(self, nickname, age, color):
		self.nickname = nickname
		self.age = age
		self.color = color
	def eat(self, food):
		print('{}喜欢吃{}'.format(self.nickname, food))
	def catch_mouse(self, color, weight):
		print('{}，抓了一只{}kg,{}的老鼠'.format(self.nickname, weight, color))

cat1 = Cat('花花', 2, '灰色')
cat1.catch_mouse('黑色', 2)
cat1.eat('鱼')
