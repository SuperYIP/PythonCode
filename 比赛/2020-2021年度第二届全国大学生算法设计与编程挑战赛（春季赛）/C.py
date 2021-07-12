n, m = input().split()
list1 = []
dict1 = {}
result = 0
for i in range(int(m) + 1):
    list1.append(list(input().replace(' ','')))
sure_num = list1[len(list1)-1][0]
sure_point = list1[int(sure_num)-1][1]
dict1[sure_point] = list1[int(sure_num)-1][2]
list1.pop()
for temp in list1:
    if temp[1] not in dict1.keys():
        dict1[temp[1]] = temp[2]
    else:
        if temp[1] != sure_point and int(temp[2]) < int(dict1[temp[1]]):
            dict1[temp[1]] = temp[2]
print(dict1)
for temp in dict1.values():
    result += int(temp)
print(result)

