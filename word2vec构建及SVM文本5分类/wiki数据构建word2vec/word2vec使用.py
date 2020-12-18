#coding=utf-8
from gensim.models import word2vec
import logging
model_1 = word2vec.Word2Vec.load(r'data\模型\wiki.model')
# 计算两个词的相似度/相关程度
y1 = model_1.similarity("赵敏", "韦一笑")
print(u"赵敏和韦一笑的相似度为：", y1)
print("-------------------------------\n")

# 计算某个词的相关词列表
y2 = model_1.most_similar("不喜欢", topn=10)  # 10个最相关的
print(u"最相关的词有：\n")
for item in y2:
    print(item[0], item[1])
print("-------------------------------\n")