#coding=utf-8
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告
import numpy as np
import pandas as pd
from gensim.models import word2vec
'''
从词向量模型中提取文本特征向量
'''
# 返回特征词向量
def getWordVecs(wordList, model):
    vecs = []
    for word in wordList:
        word = word.replace('\n', '')
        # print word
        try:
            vecs.append(model[word])
        except KeyError:
            continue
    return np.array(vecs, dtype='float')  # 返回一个二维numpy数组

# 构建文档词向量
def buildVecs(data, model):
    fileVecs = []
    for line in data:
        if(type(line) == str):	#不知道为啥列表中有float数据，输出是nan，不知道是啥
            wordList = line.split(' ')
            vecs = getWordVecs(wordList, model)
            if len(vecs) > 0:
                vecsArray = sum(np.array(vecs)) / len(vecs)  # mean
                fileVecs.append(vecsArray)
    return fileVecs

if __name__ == '__main__':
    #加载word2vec模型
    model = word2vec.Word2Vec.load(r'data\word2vec_model\wiki.model')
    #加载数据
    one_input = pd.read_csv(r'data\数据预处理后\one_jieba.csv', header=None, index_col=None)
    two_input = pd.read_csv(r'data\数据预处理后\two_jieba.csv', header=None, index_col=None)
    three_input = pd.read_csv(r'data\数据预处理后\three_jieba.csv', header=None, index_col=None)
    four_input = pd.read_csv(r'data\数据预处理后\four_jieba.csv', header=None, index_col=None)
    five_input = pd.read_csv(r'data\数据预处理后\five_jieba.csv', header=None, index_col=None)
    #提取特征向量
    one_feature = buildVecs(one_input[1][1:], model)
    two_feature = buildVecs(two_input[1][1:], model)
    three_feature = buildVecs(three_input[1][1:], model)
    four_feature = buildVecs(four_input[1][1:], model)
    five_feature = buildVecs(five_input[1][1:], model)
    #构造特征向量矩阵
    #获取各句子特征向量
    X = one_feature[:]
    X.extend(two_feature)
    X.extend(three_feature)
    X.extend(four_feature)
    X.extend(five_feature)
    X = np.array(X)
    #获取score值
    Y = np.array(one_input[0][1:len(one_feature)+1])	#上面提取特征向量时，去掉了值为nan的，这里score列数量要和其保持一致
    Y = np.append(Y,two_input[0][1:len(two_feature)+1])
    Y = np.append(Y,three_input[0][1:len(three_feature)+1])
    Y = np.append(Y,four_input[0][1:len(four_feature)+1])
    Y = np.append(Y,five_input[0][1:len(five_feature)+1])
    # write in file
    df_x = pd.DataFrame(X)
    df_y = pd.DataFrame(Y)
    data = pd.concat([df_y, df_x], axis=1)
    #保存特征向量到本地
    data.to_csv(r'data\特征向量\特征向量.csv')





