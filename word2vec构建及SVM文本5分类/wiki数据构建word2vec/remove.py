#coding=utf-8
import re
import codecs
# 4
'''
对分词后数据进行去除非中文词处理
'''
print('主程序执行开始...')

input_file_name = r'data\分词后\wiki.cn.simple.separate.txt'
output_file_name = r'data\去除非中文词\wiki.txt'
stopkey = [w.strip() for w in codecs.open(r'data\停用词表.txt', 'r', encoding='utf-8').readlines()] #广播形式获取停用词表
input_file = open(input_file_name, 'r', encoding='utf-8')
output_file = open(output_file_name, 'w', encoding='utf-8')

print('开始读入数据文件...')
lines = input_file.readlines()
print('读入数据文件结束！')

print('分词程序执行开始...')
count = 1
cn_reg = '^[\u4e00-\u9fa5]+$'

for line in lines:
    line_list = line.split('\n')[0].split(' ')
    line_list_new = []
    for word in line_list:
        if re.search(cn_reg, word):
            if word not in stopkey:
                if word != '\t':
                    line_list_new.append(word)
    output_file.write(' '.join(line_list_new) + '\n')
    count += 1
    if count % 10000 == 0:
        print('目前已分词%d条数据' % count)
print('分词程序执行结束！')

print('主程序执行结束！')