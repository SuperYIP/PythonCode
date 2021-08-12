#coding=utf-8
'''
课件
'''
# # 打开文件
# f = open(r'C:\Users\伊海迪\Desktop\1.txt', 'r', encoding='utf-8')
# content = f.read()
# print(content)
f = open(r'C:\Users\伊海迪\Desktop\朱楀墨2021-07-21的一天.txt', 'w', encoding='utf-8')
content = f.write('今天只吃了一顿饭')
f.close()



# # 打开文件
# f = open(r'C:\Users\伊海迪\Desktop\2.txt', 'w', encoding='utf-8')
# # 写内容
# content = f.write('hello python')

# # 打开文件
# f = open(r'C:\Users\伊海迪\Desktop\2.txt', 'a', encoding='utf-8')
# # 写内容
# content = f.write('\n伊海迪')