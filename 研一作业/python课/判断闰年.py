# coding=utf-8
# 保证输入的是年份
while True:
    try:
        year = eval(input("请输入一个年份\n"))
        break
    except:
        print("输入有错")
# 能被4整除但不能被100整除，或者能被400整除的年份，都是闰年
if year % 4 == 0 and year % 100 != 0:
    print("闰年")
elif year % 400 == 0:
    print("闰年")
else:
    print("不是闰年")
