# coding=utf-8


# C
import sys
result_list = []
T = int(input())
n = 0
def test(str1):
    a = 0
    b = 0
    for i in range(len(str1)):  # 遍历整个字符串
        for j in range(i + 1, len(str1)):  # 遍历第一个for循环之后的字符串
            if str1[j] == str1[i]:  # 匹配到两个相同的字符
                temp_str1 = str1[i:len(str1)];  # 舍掉字符串前不重复的部分，将剩余的切出来
                temp1 = str1[i:j]  # 两个重复字符间的字符串，大概率就是重复的字符串了
                temp2 = str1[j:len(str1)]  # 重复字符到原字符串末尾，temp_str1 = temp1 + temp2
                if len(temp2) <= len(temp1):  # 整个字符串没有两个完全重复的子字符串，子字符串只有部分重复
                    for t1, t2 in zip(temp1, temp2):
                        if t1 == t2:
                            continue
                        else:
                            break
                    else:
                        a = len(temp1) + len(temp2)
                        b = len(temp1)
                        if a % b == 0:
                            return '{}/{}'.format(a // b, 1)
                        else:
                            return '{}/{}'.format(a, b)
                else:
                    for k in range(0,len(temp2),len(temp1)):
                        if temp1 != temp2[k:k+len(temp1)]:
                            break
                    else:
                        a = len(temp_str1)
                        b = len(temp1)
                        if a % b == 0:
                            return '{}/{}'.format(a // b, 1)
                        else:
                            return '{}/{}'.format(a, b)

            else:
                continue
while n < T:
    str1 = input()
    temp = test(str1)
    result_list.append(temp)
    n += 1

for temp in result_list:
    if temp == result_list[len(result_list)-1]:
        print(temp, end='')
    else:
        print(temp)
# D 兰德索尔杯-cup
# n = int(input())
# while n > 100 or n < 1:
#     n = int(input())
# time_list = []
# for i in range(4):
#     player_in = input()
#     player = player_in[0:n]
#     sum_time = 0  # 一个选手的总时间
#     multiple = 1  # 速度倍数，初始为1
#     remain = 0  # 剩余加速时间
#     for temp in player:
#         time = 0  # 本次位置花费的时间
#         # 判断路况
#         if temp == '.':
#             if remain * (1 * multiple) >= 1:
#                 time += 1 / (1 * multiple)
#                 remain -= time
#             else:
#                 time += remain
#                 time += (1 - (remain * (1 * multiple))) / (1 * 1)
#                 multiple = 1
#                 remain = 0
#         elif temp == 'w':
#             if remain * (0.5 * multiple) >= 1:
#                 time += 1 / (0.5 * multiple)
#                 remain -= time
#             else:
#                 time += remain
#                 time += (1 - (remain * (0.5 * multiple))) / (0.5 * 1)
#                 multiple = 1
#                 remain = 0
#         elif temp == '>':
#             multiple = 2
#             remain = 5
#             time += 1 / (1 * multiple)
#             remain -= time  # 剩余加速时间，此处虽然用了1s，但还是设置为5，统一在最后if语句处减。
#         elif temp == 's':
#             time += 1
#             remain -= 1
#             if remain * (1 * multiple) >= 1:
#                 time += 1 / (1 * multiple)
#                 remain -= (time - 1)
#             else:
#                 if remain > 0:
#                     time += remain
#                     time += (1 - (remain * (1 * multiple))) / (1 * 1)
#                     multiple = 1
#                     remain = 0
#                 else:
#                     multiple = 1
#                     remain = 0
#                     time += 1 / (1 * multiple)
#         elif temp == 'm':
#             time += 2
#             remain -= 2
#             if remain * (1 * multiple) >= 1:
#                 time += 1 / (1 * multiple)
#                 remain -= (time - 2)
#             else:
#                 if remain > 0:
#                     time += remain
#                     time += (1 - (remain * (1 * multiple))) / (1 * 1)
#                     multiple = 1
#                     remain = 0
#                 else:
#                     multiple = 1
#                     remain = 0
#                     time += 1 / (1 * multiple)
#         sum_time += time
#     time_list.append(sum_time)
# # 输出
# for temp in time_list:
#     print(temp, '', end='')
