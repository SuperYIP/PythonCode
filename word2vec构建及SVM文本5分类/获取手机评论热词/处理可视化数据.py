#coding=utf-8
import pymysql
import pandas as pd
import jieba
import re
import codecs
from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
from collections import Counter
'''
处理数据库中的原始数据：获取所有评论中出现次数最多的词(形象展示每部手机的评论关键词)
'''
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
# 生成词云
def getwordcloud(text):
    wordcloud = WordCloud(
        # 设置字体，不然会出现乱码，文字的路径是电脑的字体一般路径，可以换成别的
        font_path="C:/Windows/Fonts/simkai.ttf",
        # 设置背景，宽、高
        background_color="white", width=1000, height=880).generate(text)  # 生成词云
    # wordcloud.to_file(r'F:\t\test\1.jpg')  # 保存词云图片
    # #将词云显示在屏幕上
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off") #隐藏坐标轴
    plt.show()

#获取评论中出现次数前10的词，返回形式为str
def most_num_word(sentence):
    top_ten_wordlist = []   #用于存放传入的sentence转换为列表后的数据
    top_ten_wordstr = ''    #函数返回值，数据库中没法存list，故转换为str存放
    top_ten_wordlist = Counter(sentence.split()).most_common(10)    #获得出现次数前10的列表：格式如下[('美丽', 3), ('可爱', 2)]
    for i in range(10):                                             #sentence.split();   #将字符串以空格分割，转换为列表
        top_ten_wordstr += top_ten_wordlist[i][0] + ' ' + str(top_ten_wordlist[i][1]) + ' ' #构造str，词接空格接出现次数
    return top_ten_wordstr.strip() #去除字符串首尾的空格（如果有的话）

#操作数据库：读取数据库内容
def read_mysql_data():
    dbconn = pymysql.connect(
        host = "127.0.0.1",
        database = 'jd_spider',
        user = 'root',
        password = '123456'
        )
    sql = 'select * from jd_all'
    a = pd.read_sql(sql, dbconn)    #返回的是dataframe类型数据
    return a
#向数据库中写入数据
def write_mysql_data(db_data=()):
    conn = pymysql.connect(
        host="127.0.0.1",
        database='jd_spider',
        user='root',
        password='123456'
    )
    cursor = conn.cursor()
    sql = """ INSERT INTO jd_analyse(phone_name,comment_jieba) VALUES(%s,%s) """
    cursor.execute(sql, db_data)
    conn.commit()

if __name__ == '__main__':
    a = read_mysql_data()   #获得mysql中数据，dataframe格式
    tempjiebalist = []  #定义空列表，用于暂时存放jieba分词结果
    temp = ''
    stopkey = [w.strip() for w in codecs.open(r'data\停用词表.txt', 'r', encoding='utf-8').readlines()]  # 广播形式获取停用词表
    #遍历每个手机下的所有评论
    for prephone in a['phone_name']:
        if(temp == prephone):
            continue
        else:
            temp = prephone #取值当前手机
            tempdata = a.loc[a['phone_name'].isin([prephone])]['comment']   #获得每个手机下的所有评论
            for precomment in tempdata: #遍历每条评论
                precomment = clearTxt(precomment)   #对每个手机下的每条评论进行数据清洗
                tempjiebalist.extend(jieba.lcut(precomment))    #对每条评论分词，将每部手机下的所有评论分词结果保存在一个列表下
            drop_result = delstopword(tempjiebalist, stopkey)   #去除停用词后的数据，str形式
            # getwordcloud(drop_result) #生成词云
            top_ten_word_str = most_num_word(drop_result)    #获得出现次数最多的前10个词
            write_mysql_data((prephone, top_ten_word_str))
            tempjiebalist = []  #将列表置空，准备存放下一部手机数据
