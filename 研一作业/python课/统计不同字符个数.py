# coding=utf-8
s = input("请输入一个字符串")
eng = 0  # 英文字符
num = 0  # 数字
back = 0  # 空格
other = 0  # 其他
for c in s:
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        eng += 1
    elif c >= '0' and c <= '9':
        num += 1
    elif c == ' ':
        back += 1
    else:
        other += 1
print('英文字符:', eng, ',数字:', num, ',空格:', back, ',其他:', other)
print(eng, num, back, other)
