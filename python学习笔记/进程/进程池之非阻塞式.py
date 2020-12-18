'''
非阻塞式：全部添加到队列中，立刻返回，并没有等待其他的进程执行完毕
'''

from multiprocessing import Pool
import time
from  random import random


def task(task_name):
	print('开始做任务：', task_name)
	start = time.time()
	time.sleep(random() * 2)
	end = time.time()
	return '任务完成用时：', (end - start)
container = []
def callback_func(n):
	container.append(n)

if __name__ == '__main__':
	pool = Pool(5)
	tasks = ['a','b','c','d','e','f']
	for t in tasks:
		pool.apply_async(task, args=(t), callback=callback_func)	#第一个参数：函数名，第二个参数：函数需传入的参数
	pool.close()
	pool.join()
	print('------------>over')
	for c in container:
		print(c)