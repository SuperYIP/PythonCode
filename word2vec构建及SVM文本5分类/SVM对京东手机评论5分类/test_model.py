#coding:utf-8
import numpy as np
from gensim.models import word2vec
from sklearn.svm import SVC
import joblib
import jieba
import codecs
import re
import random
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
    if(sentence == ''):
        return wordList
    else:
        return sentence.strip().split()

# 返回特征词向量
def getWordVecs(wordList, model):
    vecs = []
    for word in wordList:
        word = word.replace('\n', '')
        try:
            vecs.append(model[word])
        except KeyError:
            continue
    if(len(vecs) == 0):
        return vecs;
    else:
        return (sum(vecs) / len(vecs)).reshape(1,400)

#对单个句子进行情感判断
def svm_predict(sent):

    model = word2vec.Word2Vec.load(r'data\word2vec_model\wiki.model')
    jieba.load_userdict(r'data\dict.txt')  #读取字典
    stopkey = [w.strip() for w in codecs.open(r'data\停用词表.txt', 'r', encoding='utf-8').readlines()] #广播形式获取停用词表
    sent = clearTxt(sent)   #数据清洗
    sent_cut = jieba.lcut(sent) #分词
    drop_word_list = delstopword(sent_cut, stopkey)  #删除停用词
    sent_cut_vec = getWordVecs(drop_word_list, model)    #得到词向量
    if(len(sent_cut_vec) == 0):
        return 'no'
    else:
        clf = joblib.load(r'data\svm_model.pkl')
        result = clf.predict(sent_cut_vec)
        if (result[0] == 1):
            result_word = '非常不满意'
        if (result[0] == 2):
            result_word = '不满意'
        if (result[0] == 3):
            result_word = '一般'
        if (result[0] == 4):
            result_word = '满意'
        if (result[0] == 5):
            result_word = '非常不满意'
        return result_word
        # 自己用的~
        # list1 = ['1', '2']
        # list2 = ['4', '5']
        # result_word = ''
        # if(result[0] == 1):
        #     result_word = list1[random.randint(0,1)]
        # if (result[0] == 3):
        #     result_word = '3'
        # if (result[0] == 5):
        #     result_word = list2[random.randint(0, 1)]
        # return result_word


#情感正式开始预测
if __name__ == '__main__':
    # sent = '手机非常好'
    sent = '这手机质量也太不咋地了，妥妥的差评。。。我是刷单'
    analyse = svm_predict(sent)
    print(analyse)


