# coding=utf-8
'''
课件
'''

def func(num1, num2):
    try:
        res = num1 % num2
        return res
    except Exception as e:
        print('出现异常',e)
func(2,0)