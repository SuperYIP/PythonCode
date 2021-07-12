#coding=utf-8
x = 13930
y = 457439
num = 0
for temp in range(x, y+1):
    str_temp = str(temp)
    length = len(str_temp)
    if abs(int(str_temp[0]) - int(str_temp[length-1])) >= 2:
        for i in range(length-1):
            if abs(int(str_temp[i]) - int(str_temp[i+1])) >= 7:
                break
        else:
            num += 1
    else:
        continue