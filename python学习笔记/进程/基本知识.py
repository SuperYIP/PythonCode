'''
包含关系：进程-->线程-->协程（进程包含线程，线程包含协程）
'''
'''
创建进程：
	1. from multiprocessing import Process
	2. process = Process(target=函数名, name=进程的名字, args=给函数传递的参数）
	3. process.start() 启动任务并执行任务
	   process.run() 只是执行了任务但是没有启动进程
	   terminate() 终止
'''
from multiprocessing import Process
from time import sleep

def task1():
	while True:
		sleep(1)
		print('this is task 1')

def task2():
	while True:
		sleep(1)
		print('this is task 2')

if __name__ == '__main__':	#if __name__ == '__main__' 我们简单的理解就是： 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
	#子进程
	p = Process(target=task1)
	p.start()
	p1 = Process(target=task2)
	p1.start()