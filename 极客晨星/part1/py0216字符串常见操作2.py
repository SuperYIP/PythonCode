#coding=utf-8
'''
capitalize： 把字符串的第一个字符大写
title: 把字符串的每个单词首字母大写
startswith: startswith('obj')检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
endswith: endwith('obj')检查字符串是否以 obj 结束，如果是返回 True,否则返回 False.
lower: 转换 mystr 中所有大写字符为小写。mystr.lower()
upper: 转换 mystr 中的小写字母为大写。mystr.upper()
ljust: 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串。mystr.ljust(width)
rjust: 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。mystr.rjust(width)
center: 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。mystr.center(width)
strip: 删除 mystr 左边的空白字符。mystr.lstrip()
rstrip: 删除 mystr 字符串末尾的空白字符。mystr.rstrip()
strip: 删除 mystr 字符串两端的空白字符
join:  join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
'''

str1 = '  hello  '
# print(str1.capitalize())
# print(str1.title())
# print(str1.startswith('zhang'))
# print(str1.endswith('zhang'))
# print(str1.lower())
# print(str1.upper())
# print(str1)
# print(str1.ljust(20))
# print(str1.rjust(20))
# print(str1.center(20))
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())
# str2 = '-'
# # str3 = 'python'
# print(str2.join(str1))

# # 课堂练习
# var = input("请输入一个变量名：").strip()
# # 判断第一个字符是否合法
# if var[0] == "_" or var[0].isalpha():
#     for char in var[1:]: # 判断除了第一个字符之外的其他字符是否合法
#         if not (char.isalnum() or char == "_"):
#             print("变量名%s 不合法" % var)
#             break
#     else:
#         print("变量名%s 合法" % var)
# else:
#     print("变量名不合法，第一个字符错误")

var = input('请输入一个变量名：').strip()
if var[0] == '_' or var[0].isalpha():
    for char in var[1:]:
        if not(char.isalnum() or char =='_'):
            print('变量名不符合规范')
            break
    else:
        print('变量名符合规范')
else:
    print('第一个字符不符合规范')