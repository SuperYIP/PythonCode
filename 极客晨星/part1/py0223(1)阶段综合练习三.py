#coding=utf-8
'''
课件
'''

# # 1.
# l = ['Hello', 'World', 'IBM', 'Apple']
# l1 = [s.lower() for s in l]
# print(l1)

# # 2
# str1 = input('请输入字符串1：')
# str2 = input('请输入字符串2：')
# str3 = ''
# for s in str1:
#     if s in str2:
#         pass
#     else:
#         str3 += s
# print(str3)

# 3
name = []
number = []
a = '''
----通讯录管理系统----
1. 增加姓名和手机
2. 删除姓名
3. 修改手机
4. 查询所有用户
5. 根据姓名查找手机号
6. 退出
--------------------
请选择：
'''

# while True:
#     choice = int(input(a))
#     if choice not in range(1,7):
#         input('输入有误，请重新输入：')
#     else:
#         if choice == 1:
#             name1 = input('请输入姓名：')
#             if name1 in name:
#                 print('已经有这个联系人，请重新输入')
#                 continue
#             else:
#                 name.append(name1)
#                 number1 = input('请输入手机号：')
#                 number.append(number1)
#                 print('写入完成')
#         elif choice == 2:
#             name1 = input('请输入要删除的联系人姓名：')
#             if name1 in name:
#                 name.remove(name1)
#                 print('删除完成')
#             else:
#                 print('没有这个联系人，请重新输入')
#                 continue
#         elif choice == 3:
#             name1 = input('请输入要修改的联系人姓名：')
#             if name1 in name:
#                 index = name.index(name1)
#                 number1 = input('请输入要修改的手机号：')
#                 number[index] = number1
#                 print('修改完成')
#             else:
#                 print('没有这个联系人，请重新输入')
#                 continue
#         elif choice == 4:
#             print('所有用户如下：')
#             for temp in name:
#                 print(temp)
#         elif choice == 5:
#             name1 = input('请输入要查找的联系人姓名：')
#             if name1 in name:
#                 index = name.index(name1)
#                 print('您要查找的手机号是：', number[index])
#             else:
#                 print('没有这个联系人，请重新输入')
#                 continue
#         elif choice == 6:
#             print('感谢使用')
#             break
#         else:
#             print('输入有误，请重新输入')
#             continue
