# 继承：is a ， has a
'''
1. has a
	一个类中使用了另一种自定义的类型
2. 类型
	系统类型：str int list ...
	自定义类型：类 ...
'''
'''
2. is a -->继承
'''
import random


class Road:
	def __init__(self, name, len):
		self.name = name
		self.len = len


class Car:
	def __init__(self, brand, speed):
		self.brand = brand
		self.speed = speed

	def get_time(self, road):
		ran_time = random.randint(1, 10)
		msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, ran_time)
		print(msg)

	def __str__(self):
		return '{}品牌的，速度：{}'.format(self.brand, self.speed)


r = Road('京藏高速', 12000)
audi = Car('奥迪', 100)
print(audi)
