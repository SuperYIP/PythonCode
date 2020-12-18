#coding=utf-8
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
# 5
'''
构建word2vec模型
'''
if __name__ == "__main__":
    print('主程序开始执行...')

    input_file_name = r'data\去除非中文词\wiki.txt'
    model_file_name = r'data\模型\wiki.model'

    print('转换过程开始...')
    model = Word2Vec(LineSentence(input_file_name),
                     size=400,  # 词向量长度为400
                     window=5,
                     min_count=5,
                     workers=multiprocessing.cpu_count())
    print('转换过程结束！')

    print('开始保存模型...')
    model.save(model_file_name)
    print('模型保存结束！')

    print('主程序执行结束！')