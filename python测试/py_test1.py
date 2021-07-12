#coding=utf-8
import re
# str1 = '2018/3/1'
# str2 = '018-04-01'
# # pattern = re.compile('^\d{1,2}')
# pattern = re.compile('/(\d){1}/')
# # pattern = re.compile('/(\d){1,2}$')
# pattern = re.compile('-(\d){1,2}$')
# match = pattern.search(str2)
# day = match.group()[1:]
# print(day)
# day = day.replace(day[0], '')
# print(day)
# print(match  == None)

# #day
# str1 = '2018/4/5'
# pattern = re.compile('/(\d){1,2}$')
# match = pattern.search(str1)
# day = day = match.group()[1:]
# print(day)

# month
# str1 = '2020/11/1'
str2 = '018-04-01'
# pattern = re.compile('/(\d){1,2}/')
pattern = re.compile('-(\d){2}-')
match = pattern.search(str2)
month = match.group()[1:3]
print(month)
if len(month) == 2 and month[0] == '0':  #去掉04这种month格式的0，保持所有month格式一致
	month = month.replace(month[0], '')
print(month)
print(str2[5])
# # hour
# list1 = []
# str1 = '23:00:00'
# pattern = re.compile('^\d{1,2}')
# match = pattern.search(str1)
# hour = int(match.group())
# print(hour)
# print(type(hour))
# list1.append(hour)
# print(list1)