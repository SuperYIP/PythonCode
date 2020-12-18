#私有化
'''
封装：
	1. 私有化属性
	2. 定义公有set和get方法
__属性：将属性私有化，访问范围仅仅限在类中
好处：
	1. 隐藏属性不被外界随意修改
	2. 通过函数修改，可以筛选赋值内容是否符合条件
'''

class Student():
	# __age = 18

	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		self.__score = 59
	# #定义set和get方法（旧版）
	# def setAge(self, age):
	# 	if(age>0 and age<120):
	# 		self.__age = age
	# 	else:
	# 		print('年龄不符合条件')
	# def getAge(self):
	# 	return self.__age

	# 定义set和get方法（新版）,使用@property装饰器
		#先有get，再有set
	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self, age):
		if(age>0 and age<120):
			self.__age = age
		else:
			print('年龄不符合条件')
	def __str__(self):
		return '姓名：{}，年龄：{}，考试分数：{}'.format(self.__name, self.__age, self.__score)

# #老版测试
# xiaoyi = Student('xiaoyi', 19)
# print(xiaoyi)
# print(dir(Student))
# print(dir(xiaoyi))	#可以看到私有化只不过是伪装成私有，__属性，在底层被修改为，_类名__属性，通过对象._类名__属性还是可以直接访问
# print(xiaoyi._Student__age)	#此处可以访问age

#新版测试
s = Student('xiaoyi', 20)
print(s.age)
s.age = 30
print(s.age)