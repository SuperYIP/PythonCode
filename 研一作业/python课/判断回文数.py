# coding=utf-8
n = input("请输入一个数字n：")
l = len(n) // 2
flag = True
while l > 0:
    if n[l - 1] != n[-l]:
        flag = False
        print("no")
        break
    l = l - 1
if flag == True:
    print('yes')
