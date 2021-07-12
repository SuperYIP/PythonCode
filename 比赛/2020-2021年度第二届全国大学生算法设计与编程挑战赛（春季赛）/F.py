# n, m = input().split()
# list1 = []
# result_list = []
# for i in range(int(m)):
#     list1.append(list(input().replace(' ','')))
# print(list1)
# # for i in range(len(list1)):
# #     result = 0
# #     if list1[i][0] == '1':
# #         movie = list1[i][1]
# #         for j in range(i):
# #             k = list1[j]
# #             if k[0] != '1' and (int(movie) < int(k[1]) or int(movie) > int(k[2])):
# #                 result += (int(k[3]) * (int(k[2]) - int(k[1]) + 1))
# #     if result != 0:
# #         result_list.append(result)
# # for temp in result_list:
# #     if temp == result_list[len(result_list) - 1]:
# #         print(temp, end='')
# #     else:
# #         print(temp)


# for temp in list1:
#     result = 0
#     if temp[0] == '1':
#         move = temp[1]
#         for k in list1:
#             if len(k) == 4 and move not in k:
#                 result += (int(k[3]) * (int(k[2]) - int(k[1]) + 1))
#     if result != 0:
#         print(result)

# str1 = input().replace(' ','')
# m = int(input())
# for i in range(m):
#     l, r = input().split()
#     temp_str1 = str1[l-1:r]

# F
n, m = input().split()
list1 = []
result_list = []
for i in range(int(m)):
    list1.append(list(input().replace(' ','')))
for i in range(len(list1)):
    result = 0
    if list1[i][0] == '1':
        movie = list1[i][1]
        for j in range(i):
            k = list1[j]
            if k[0] != '1' and (int(movie) < int(k[1]) or int(movie) > int(k[2])):
                result += (int(k[3]) * (int(k[2]) - int(k[1]) + 1))
        result_list.append(result)
for temp in result_list:
    if temp == result_list[len(result_list) - 1]:
        print(temp, end='')
    else:
        print(temp)