#进程：自定义
from multiprocessing import Process
class MyProcess(Process):
	def __init__(self, name):
		super().__init__()
		self.name = name
	#重写run方法
	def run(self):
		n = 1
		while True:
			print('{}---->自定义进程:{}'.format(n, self.name))
			n += 1

if __name__ == '__main__':
	p = MyProcess('小米')
	p.start()
	p1 = MyProcess('小白')
	p1.start()