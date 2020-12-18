#coding = utf-8
class Person:
	def __init__(self, number, name, salary):
		self.number = number
		self.name = name
		self.salary = salary

	def __str__(self):
		msg = '工号：{}，姓名{}，本月工资{}'.format(self.number, self.name, self.salary)
		return msg

	def getSalsry(self):
		return self.salary


class Worker(Person):
	def __init__(self, number, name, salary, hours, per_hour):
		super().__init__(number, name, salary)
		self.hours = hours
		self.per_hour = per_hour

	def getSalsry(self):
		money = self.hours * self.per_hour
		self.salary += money
		return self.salary

class Salesman(Person):
	def __init__(self, number, name, salary, salemoney, percent):
		super().__init__(number, name, salary)
		self.salemoney = salemoney
		self.percent = percent
	def getSalsry(self):
		money = self.salemoney * self.percent
		self.salary += money
		return self.salary

w = Worker('001', 'yi', 2000, 160, 100)
s = w.getSalsry()
print('月薪是：', s)