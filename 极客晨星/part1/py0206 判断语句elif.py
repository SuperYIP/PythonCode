'''
之前讲了if else语句，但是如果有多个条件需要判断，则单纯使用if else不能实现
本节讲if elif else，对需要多个条件要判断的情况，进行解决
'''

# chengji = 75
# if chengji >=90 and chengji <=100:
#     print("等级为A")
# elif chengji >= 80 and chengji <=89:
#     print("等级为B")
# elif chengji >= 70 and chengji <=79:
#     print("等级为C")
# else :
#     print("等级为C.5")

# num1 = int(input("请输入要计算的第一个数："))
# operator = input("请输入运算符号：")
# num2 = int(input("请输入要计算的第二个数："))
# if operator == '+':
#     print(num1 + num2)
# elif operator == '*':
#     print(num1 * num2)
# elif operator == '-':
#     print(num1 - num2)
#     print('计算完毕')
# elif operator == '/':
#     print(num1 / num2)
# else:
#     print("只能输入加减乘除，请重新输入")
#
# num1 = int(input("请输入数字："))
# fuhao = input("请输入符号：")
# num2 = int(input("请输入数字:"))
# if fuhao == '+':
#     print(num1 + num2)
# elif fuhao == '-':
#     print(num1 - num2)



# num1 = int(input("请输入数字："))
# fuhao = input("请输入符号：")
# num2 = int(input("请输入数字:"))
# if fuhao == '+':
#     print(num1 + num2)
# elif fuhao == '-':
#     print(num1 - num2)
# elif fuhao == '*':
#     print( num1+ num2)
# elif fuhao == '÷':
#     print(num1+ num2)







# 获取身高
# height = float(input("请输入你的身高(m)："))    # 注意输入的单位
# # 获取体重
# num2 = float(input("请输入你的体重(kg)："))
#     # 这里可以加入if语句判断输入的身高体重是否合理，如正常身高大致应在1.5-2.0之间
# # 计算BMI值
# bmi = num2 / (height * height)  # 公式
# print("你的BMI指数是：%.2f" % bmi)    # 也可以用format实现
# # if-elif-else
# if bmi < 18.5:
#     print("过轻")
# elif 18.5 <= bmi < 25:
#     print("正常")
# elif 25 <= bmi < 28:
#     print("过重")
# elif 28 <= bmi < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# import random
# player = int(input('请输入：剪刀（0），石头（1），布（2）：'))
# computer = random.randint(0,2)
# print('电脑出 %d' % computer)
# if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#     print('用户赢')
# elif player == computer:
#     print('平局')
# else:
#     print('用户输')
