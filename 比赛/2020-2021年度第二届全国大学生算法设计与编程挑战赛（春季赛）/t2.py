# A
# a_1 = 1
# a_2 = 2
# a_3 = 5
# mod = 100000
# for i in range(4, 1000 + 1):
#     temp = a_1 * a_2 * a_3 + a_1 + a_2 + a_3
#     temp %= mod
#     a_1 = a_2
#     a_2 = a_3
#     a_3 = temp
# print(a_3)


# D
# import time
# start = time.clock()
# n,q = input().split()
# str1 = input().replace(' ','')
# # str1 = str1.replace(' ','')
# result_list = []
# for i in range(0, int(q)):
#     l,r,k = input().split()
#     l = int(l)  # 左
#     r = int(r)  # 右
#     k = int(k)  # 个数
#     temp_str1 = str1[l-1:r]
#     result = 0
#     for temp in temp_str1:
#         if temp_str1.count(temp) == k:
#             result += 1
#     result_list.append(result)
# for temp in result_list:
#     print(temp)
# end = time.clock()
# print(int((end-start)*1000))

# from collections import Counter
# n,q = input().split()
# str1 = input().replace(' ','')
# for i in range(0, int(q)):
#     l,r,k = input().split()
#     temp_str1 = str1[int(l)-1:int(r)]
#     result = 0
#     for temp in temp_str1:
#         if temp_str1.count(temp) == int(k):
#             result += 1
#     print(result)


# F
# n,q = input().split()
# str1 = input().replace(' ','')
# m = int(input())
# for i in range(m):
#     l, r = input().split()
#     temp_str1 = str1[l-1:r]


