#coding=utf-8
'''

'''

# 1
# def scrabble_score(s):
#     score = {
#         'a':1, 'c':3, 'w':4, 'o':1, 'r':1, 'd':2
#     }
#     sum = 0
#     l = list(s.lower())
#     for temp in l:
#         if temp in score.keys():
#            sum += score[temp]
#     return sum
# print(scrabble_score('Word'))

# 2
# n = int(input('请输入一个整数：'))
# d = {}
# for i in range(1, n+1):
#     d[i] = i*i
# print(d)

# 3
# def collatz(num):
#     if num % 2 == 0:
#         print(num // 2)
#         return num // 2
#     else:
#         print(3 * num + 1)
#         return 3 * num + 1
# num = int(input('请输入数字：'))
# i = 0
# while i != 1:
#     i = collatz(num)
#     num = i

# 4
# def input_file(name, sex, age, education):
#     f = open(r'C:\Users\伊海迪\Desktop\1.txt', 'a', encoding='utf-8')
#     content = '\n' . join([name, sex, age, education])  # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#     f.write(content)
# name = input('请输入您的姓名：')
# sex = input('请输入您的性别：')
# age = input('请输入您的年龄：')
# education = input('请输入您的学历：')
# input_file(name, sex, age, education)

# 5
# def input_file_pro(name, age, education, sex='男'):
#     f = open(r'C:\Users\伊海迪\Desktop\1.txt', 'a', encoding='utf-8')
#     content = '\n' . join([name, sex, age, education])  # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#     f.write(content)
#
# while True:
#     name = input('请输入您的姓名：')
#     if name.strip().upper() == 'Q': # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#         break
#     else:
#         sex = input('请输入您的性别：')
#         age = input('请输入您的年龄：')
#         education = input('请输入您的学历：')
#     input_file_pro(name, age, education, sex)
#     print('输入成功')

