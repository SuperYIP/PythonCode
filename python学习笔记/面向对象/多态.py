
#多态
'''
面向对象特点：封装 继承 多态
'''

class Person:
	def __init__(self, name):
		self.name = name
	def feed_pet(self, pet):
		if isinstance(pet, Pet):	#使用isinstance实现多态
			print('{}喜欢养宠物：{}'.format(self.name, pet.nickname))
		else:
			print('no')
class Pet:
	role = 'Pet'
	def __init__(self, nickname, age):
		self.nickname = nickname
		self.age = age
	def show(self):
		print('昵称：{}，年龄：{}'.format(self.nickname, self.age))
class Cat(Pet):
	role = '猫'
	def catch_mouse(self):
		print('抓老鼠')
class Dog(Pet):
	role = '狗'
	def watch_house(self):
		print('看家')

cat = Cat('花花', 2)
dog = Dog('大黄', 4)
person = Person('小伊')
person.feed_pet(cat)