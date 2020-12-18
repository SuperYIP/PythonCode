#单例模式
#开发模式：单例模式，优化地址空间使用（无论创建多少个实例都使用同一个地址）

class Singleton:
	__instance = None	#私有化
	#重写__new__
	def __new__(cls, *args, **kwargs):
		print('--->__new__')
		if cls.__instance is None:
			print('---->1')
			cls.__instance = object.__new__(cls)	#产生一块地址，赋值给__instance
		else:
			print('____>2')
			return cls.__instance

s = Singleton()
s1 = Singleton()