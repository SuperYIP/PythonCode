# coding=utf-8
'''
课件
'''
# f = open(r'C:\Users\伊海迪\Desktop\1.txt', 'r', encoding='utf-8')
# content = f.read(5)
# print(content)
# content = f.read()
# print(content)
# f.close()
# content = f.readline()
# print(content)
# for temp in content:
#     print(temp)

# 课堂练习
# import time
# data = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# # print(data)
# def writeNote():
#     print('请输入日记内容，结束请换行输入end：')
#     datapath = 'C:\\Users\\伊海迪\\Desktop\\' + data + '.txt'
#     f = open(datapath, 'a', encoding='utf-8')
#     while True:
#         line = input()
#         if line == 'end':
#             break
#         f.write(line + '\n')
#     f.close()
# writeNote()