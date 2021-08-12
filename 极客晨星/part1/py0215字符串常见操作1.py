# coding=utf-8
'''
课件
'''

# mystr = 'hello world python and pythoncpp'
# name = '  '
# print(name.isspace())


# print(mystr.count('python'))
# str1 = 'pypt hon'
# output = str1.isalpha()
# print(output)





str1 = input('请输入一串字符：')
letters, space, digit, other = 0, 0, 0, 0
for temp in str1:
    if temp.isalpha():
        letters += 1
    elif temp.isspace():
        space += 1
    elif temp.isdigit():
        digit += 1
    else:
        other += 1
print('字母有{}个，空格有{}个，数字有{}个，其他有{}个'.format(letters,space,digit,other))


