# coding=utf-8
'''
课件
'''

# abab = 0
# while abab < 10:
#     print('woaibeijing,woaibeijingtiananmen')
#     print('abab = %d' % abab)
#     abab += 1


# i = 0
# while i < 10:
#     print('*', end='')
#     i += 1





# num = int(input('请输入一个数字：'))    # 强制类型转换
# if num >= 1:
#     if num <= 9:
#         print('这个数字在1-9之间')
#     else:
#         print('这个数字不在1-9之间')
# else:
#     print('输入有误')
#
# chePiao = 1     # 1代表有车票，0代表没有车票
# dao = 1         # 1代表有刀，0代表没刀
# if chePiao == 1:
#     print('有车票，可以进站')
#     if dao == 0:
#         print('通过安检')
#     else:
#         print('有刀，没有通过安检，抓走！！！')
# else:
#     print('没有车票，不能进站')



# yue = 4     # 余额
# zuowei = 1  # 1代表有座位，0代表没有座位
# if yue > 2:
#     print('可以上车')
#     if zuowei == 1:
#         print('有座位，可以坐下~')
#     else:
#         print(('没有座位，站着吧~'))
# else:
#     print('不能上公交车')

# 判断数字是否在1-9之间
# num = int(input('请输入一个数字：'))
# if num >= 1:
#     if num <= 9:
#         print('数字在1-9之间')
#     else:
#         print('数字大于9')
# else:
#     print('数字小于1')
# if num >= 1 and num <= 9:
#     print('数字在1-9之间')
# else:
#     print('数字不在1-9之间')

weather = int(input('请输入天气，晴天(1),雨天(0)：'))
ice = 1 # 有冰淇淋(1),无(0)
mood = 1 # 心情好(1),不好(0)
if weather == 1:
    print('天气不错，去逛商场')
    if ice == 1:
        print('有冰淇淋，可以吃')
        if mood == 1:
            print('今天心情不错，吃一个')
        else:
            print('今天心情不好，不吃了')
    else:
        print('没有冰淇淋，吃不到了')
else:
    print('下雨天，不出门')