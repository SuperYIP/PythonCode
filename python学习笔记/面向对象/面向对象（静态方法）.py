#coding = utf-8

#讲解静态方法
'''
与类方法很类似
特点
1. 需要装饰器@staticmethod
2. 静态方法是无法传递参数的（self，cls）
3. 也只能访问类的属性和方法，对象的是无法访问的1
4. 加载时机同类方法

总结：
	类方法	静态方法
不同：
	1. 装饰器不同
	2. 类方法有参数，静态方法没有参数
相同：
	1. 只能访问类的属性和方法，对象的是无法访问的
	2. 都可以通过类名调用访问
	3. 都可以在创建对象之前使用，因为是不依赖于对象的

	普通方法 与 两者区别
不同：
	1. 没有装饰器
	2. 普通方法永远是依赖于对象，因为每个普通方法都有一个self
	3. 只有创建了对象才可以调用普通方法，否则无法调用

'''