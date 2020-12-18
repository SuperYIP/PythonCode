# coding = utf-8
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def eat(self, name):
		print('{}正在吃饭'.format(name))

	def run(self, name):
		print('%s正在跑步' % name)


class Student(Person):
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self.grade = grade

	def eat(self, food):
		super().eat(self.name)
		print('{}正在吃饭，吃的是{}，年龄是{}'.format(self.name, food, self.age))


s = Student('yi', 20, 90)
s.eat('烧鸡')

'''
另：
	python允许多继承
	多继承的搜索顺序：（代码中：对象.__mro__打印搜索顺序）
		经典类：广度优先
		新式类：广度优先
'''