# coding=utf-8
def prime(num):
    for i in range(2, num + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i, end=' ')
prime(200)
