#coding=utf-8
import jieba
import pandas as pd
import re
import codecs
'''
进行数据清洗和结巴分词，并去除停用词
'''
#加载数据，返回清洗后数据
def loaddata(datapath):
    #利用pandas读取数据文件
    data = pd.read_csv(datapath, header=None, index_col=None) # header=None 表示文件的第一行不是列的名字，是数据
    #数据清洗（读取的数据为列表，data[0]为文本列表，data[0][i]为每条数据）
    for i in range(1, len(data[3])):
        data[3][i] = clearTxt(data[3][i])
    return data

#数据清洗
def clearTxt(line):
    if line != '':
        line = line.strip()	#去除文本前后空格
        #去除文本中的英文和数字
        line = re.sub("[a-zA-Z0-9]","",line)
        #去除文本中的中文符号和英文符号
        line = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+", "",line)
    return line

#删除停用词
def delstopword(wordList,stopkey):
    sentence = ""
    for word in wordList:
        word = word.strip()
        if word not in stopkey:
            if word != '\t':
                sentence += word + " "
    return sentence.strip()

#存储到csv文件
def savedata(savepath, col1, data1, col2, data2):
    dataframe = pd.DataFrame({col1: data1, col2:data2})
    dataframe.to_csv(savepath, index=False)

if __name__ == '__main__':
    # 读入数据，得到清洗后结果，返回形式为列表
    jieba.load_userdict(r'data\dict.txt')  #读取字典

    one = loaddata(r'data\原始数据\one.csv')
    two = loaddata(r'data\原始数据\two.csv')
    three = loaddata(r'data\原始数据\three.csv')
    four = loaddata(r'data\原始数据\four.csv')
    five = loaddata(r'data\原始数据\five.csv')
    # 分词，结果返回列表
    one_cut_list = [jieba.lcut(one[3][i]) for i in range(1, len(one[3]))]  # 使用for循环来获得分词后得到的每一个词语，返回一个列表
    two_cut_list = [jieba.lcut(two[3][i]) for i in range(1, len(two[3]))]
    three_cut_list = [jieba.lcut(three[3][i]) for i in range(1, len(three[3]))]
    four_cut_list = [jieba.lcut(four[3][i]) for i in range(1, len(four[3]))]
    five_cut_list = [jieba.lcut(five[3][i]) for i in range(1, len(five[3]))]
    #去掉停用词，结果返回one['d_w']列表
    stopkey = [w.strip() for w in codecs.open(r'data\停用词表.txt', 'r', encoding='utf-8').readlines()] #广播形式获取停用词表
    one_drop_list = [delstopword(line, stopkey) for line in one_cut_list]
    two_drop_list = [delstopword(line, stopkey) for line in two_cut_list]
    three_drop_list = [delstopword(line, stopkey) for line in three_cut_list]
    four_drop_list = [delstopword(line, stopkey) for line in four_cut_list]
    five_drop_list = [delstopword(line, stopkey) for line in five_cut_list]
    # 存数据到csv
    savedata(r'data\数据预处理后\one_jieba.csv', 'score', one[2][1:], 'one_comment_jieba', one_drop_list)
    savedata(r'data\数据预处理后\two_jieba.csv', 'score', two[2][1:], 'two_comment_jieba', two_drop_list)
    savedata(r'data\数据预处理后\three_jieba.csv', 'score', three[2][1:], 'three_comment_jieba', three_drop_list)
    savedata(r'data\数据预处理后\four_jieba.csv', 'score', four[2][1:], 'four_comment_jieba', four_drop_list)
    savedata(r'data\数据预处理后\five_jieba.csv', 'score', five[2][1:], 'five_comment_jieba', five_drop_list)