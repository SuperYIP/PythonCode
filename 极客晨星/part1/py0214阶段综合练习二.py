# coding=utf-8
'''
课件
'''

# # 1.猜年龄游戏
# age = 73
# i = 1
# while i <= 3:
#     temp_age = int(input('请输出您的猜的年龄：'))
#     if temp_age == age:
#         print('恭喜您，猜对了')
#         break
#     else:
#         i += 1
#         print('猜错了，您还剩{}次机会'.format(4 - i))
#         if i == 4:
#             choice = input('是否继续新的一轮(y/n)：')
#             if choice == 'y':
#                 i = 1
#             else:
#                 print('游戏结束')

# 2. 打印所有水仙花数
# for num in range(100, 1000):
#     a = num // 100
#     b = (num - a * 100) // 10
#     c = num - a * 100 - b * 10
#     if (a ** 3 + b ** 3 + c ** 3) == num:
#         print('{}是水仙花数'.format(num))

# 3. 输出100以内的所有素数
# count = 0
# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#         count += 1
# print('共有{}个素数'.format(count))


# 4. 计算给定数字的阶乘
# a = int(input('请输入一个数字：'))
# result = 1
# for i in range(1, a+1):
#     result *= i
# print(result)

# a = int(input('请输入一个数字：'))
# result = 1
# for i in range(1, a+1):
#     result *= i
# print('{}的阶乘是{}'.format(a,result))

# 5.
# result = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         result -= i
#     else:
#         result += i
# print(result)

# result = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         result -= i
#     else:
#         result += i
# print(result)