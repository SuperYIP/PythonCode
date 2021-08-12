# coding=utf-8
'''
课件
'''
# 常规版
# def bubbleSort(arr):
#     for i in range(len(arr)-1):     # 外层n-1次，两两比较，n个元素需要比较n-1次
#         for j in range(len(arr)-1-i):   # 内层n-1-i次，因为每次遍历可以得到一个数的正确位置
#             if arr[j] > arr[j+1]:   # 将大数向后移，每轮排序可以确定一个最大数的位置
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print('第{}轮第{}趟结果为：{}'.format(i+1, j+1, arr))
#         print('第{}轮最终结果为：{}'.format(i + 1, arr),'\n','-'*30)
#     return arr

# 优化版1.0（某一轮冒泡，数组没有元素位置改变，说明已经完成排序，可以停止）（优化的是外层循环）
# def bubbleSort_pro(arr):
#     for i in range(len(arr)-1):     # 外层n-1次，两两比较，n个元素需要比较n-1次
#         flag = 1    # 设置一个标志位，判断一轮冒泡，数组是否有元素位置改变
#         for j in range(len(arr)-1-i):   # 内层n-1-i次，因为每次遍历可以得到一个数的正确位置
#             if arr[j] > arr[j+1]:   # 将大数向后移，每轮排序可以确定一个最大数的位置
#                 flag = 0    # 有改变，则将其置为0
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print('第{}轮第{}趟结果为：{}'.format(i + 1, j + 1, arr))
#         print('第{}轮最终结果为：{}'.format(i + 1, arr), '\n', '-' * 30)
#         if flag == 1:   # 一次冒泡中没有交换过元素
#             return arr
#     return arr

# # 优化版2.0（在1.0的基础上，记录每轮冒泡时交换的最后一个元素位置，这个元素之后的序列已经有序，不需要再比较）（优化的是内层循环）
# def bubbleSort_pro_2(arr):
#     pos = 0     # 记录循环里最后一次交换的位置
#     n = len(arr) - 1
#     for i in range(len(arr)-1):     # 外层n-1次，两两比较，n个元素需要比较n-1次
#         flag = 1    # 设置一个标志位，判断一轮冒泡，数组是否有元素位置改变
#         for j in range(n):   # 内层n-1-i次，因为每次遍历可以得到一个数的正确位置
#             if arr[j] > arr[j+1]:   # 将大数向后移，每轮排序可以确定一个最大数的位置
#                 flag = 0    # 有改变，则将其置为0
#                 pos = j     # 循环里最后一次交换的位置 j赋给pos
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print('第{}轮第{}趟结果为：{}'.format(i + 1, j + 1, arr))
#         print('第{}轮最终结果为：{}'.format(i + 1, arr), '\n', '-' * 30)
#         n = pos
#         if flag == 1:   # 一次冒泡中没有交换过元素
#             return arr
#     return arr
#
# # 优化版3.0 每轮排序确定一个最大值位置和一个最小值位置，正向扫描找到最大值交换到最后，反向扫描找到最小值交换到最前面
# def bubbleSort_pro_3(arr):
#     pos = 0     # 记录循环里最后一次交换的位置
#     n = len(arr) - 1
#     for i in range(len(arr)-1):     # 外层n-1次，两两比较，n个元素需要比较n-1次
#         # 正向扫描找到最大值交换到最后
#         flag = 1    # 设置一个标志位，判断一轮冒泡，数组是否有元素位置改变
#         for j in range(n):   # 内层n-1-i次，因为每次遍历可以得到一个数的正确位置
#             if arr[j] > arr[j+1]:   # 将大数向后移，每轮排序可以确定一个最大数的位置
#                 flag = 0    # 有改变，则将其置为0
#                 pos = j     # 循环里最后一次交换的位置 j赋给pos
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print('第{}轮第{}趟正向排序结果为：{}'.format(i + 1, j + 1, arr))
#         n = pos
#         if flag == 1:   # 一次冒泡中没有交换过元素
#             return arr
#         # 反向扫描找到最小值交换到最前面
#         for j in range(n,0,-1):
#             if arr[j] < arr[j-1]:
#                 flag = 0
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             print('第{}轮第{}趟反向排序结果为：{}'.format(i + 1, j + 1, arr))
#         if flag == 1:   # 一次冒泡中没有交换过元素
#             return arr
#     return arr
#
# list1 = [10,5,3,40,200]
# print(bubbleSort_pro_3(list1))

