# coding=utf-8
'''
课件
'''
# a,b = 1,2
# print(a,b)
# temp = a
# a = b
# b = temp
# print(a,b)


#     # 判断闰年
# year = int(input("请输入年份："))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("是闰年")
# else:
#     print("不是闰年")

# score = int(input('请输入成绩：'))
# if score >=90 and score <100:
#     print('优秀')
# elif score >= 70 and score <90:
#     print('良好')
# elif score >= 60 and score <70:
#     print('及格')
# else:
#     print('不及格')

score = int(input('请输入成绩：'))
if score >= 0 and score <= 100:
    if score >= 90 and score <= 100:
        print('优秀')
    elif score >= 70 and score < 90:
        print('良好')
    elif score >= 60 and score < 70:
        print('及格')
    else:
        print('不及格')
else:
    print('成绩输入有误')

# 判断成绩
# score = int(input('请输入你的成绩：'))
# if score >= 90:
#     print('优秀')
# elif score >= 70 and score < 90:
#     print('良好')
# elif score >= 60 and score < 70:
#     print('及格')
# else:
#     print('不及格')

# name = 'yihaidi'
# password = '123456'
# i = 1
# while i <= 3:
#     temp_name = input('请输入用户名：')
#     temp_password = input('请输入密码：')
#     if temp_name == name and temp_password == password:
#         print('恭喜您，登录成功')
#         break
#     else:
#         print('登录失败，您还剩{}次机会'.format(3-i))
#         i += 1
#         if i == 4:
#             print('不好意思，您没有机会了')

# name = 'python'
# password = '123'
# i = 1
# while i <= 3:
#     temp_name = input('请输入用户名:')
#     temp_password = input('请输入密码:')
#     if temp_name == name and temp_password == password:
#         print('恭喜您，登录成功')
#         break
#     else:
#         print('登录失败，您还剩{}次机会'.format(3 - i))
#         i += 1
#         if i == 4:
#             print('不好意思，您没有机会了')

# 用户登录
# name = 'python'
# password = '123'
# i = 1
# while i <= 3:
#     temp_name = input('请输入您的用户名：')
#     temp_password = input('请输出您的密码：')
#     if temp_name == name and temp_password == password:
#         print('恭喜您，登录成功')
#         break
#     else:
#         i += 1
#         if i == 4:
#             print('不好意思，你没有机会了')
#         else:
#             print('登录失败，您还剩{}次机会'.format(4-i))

# for i in range(1, 11):
#     if i >= 3 and i <= 9:
#         print('*', end='')
#         print(' ' * (i - 2), end='')
#         print('*')
#     else:
#         print('*' * i)

# for i in range(5):
#     if i == 2 or i == 3:
#         print('*', end='')
#         print(' ' * (i - 1), end='')
#         print('*')
#     else:
#         for j in range(i + 1):
#             print('*', end='')
#         print()

# 打印三角形
# for i in range(1, 6):
#     if i == 3 or i == 4:
#         print('*', end='')
#         print(' ' * (i-2), end='')
#         print('*')
#     else:
#         print('*' * i)

# for i in range(5):
#     print(" " * (4 - i), end="")
#     print("* " * (i + 1))


# for i in range(5):
#     print(' ' * (4 - i), end='')
#     print('* ' * (i + 1))
