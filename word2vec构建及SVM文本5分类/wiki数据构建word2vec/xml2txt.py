#coding=utf-8
from gensim.corpora import WikiCorpus
'''
1
这个代码是将从网络上下载的xml格式的wiki百科训练语料转为txt格式
'''
if __name__ == '__main__':

    print('主程序开始...')

    input_file_name = r'data\原始数据\zhwiki-latest-pages-articles.xml.bz2'
    output_file_name = r'data\xml转为txt\wiki.cn.txt'
    print('开始读入wiki数据...')
    input_file = WikiCorpus(input_file_name, lemmatize=False, dictionary={})
    print('wiki数据读入完成！')
    output_file = open(output_file_name, 'w', encoding="utf-8")

    print('处理程序开始...')
    count = 0
    for text in input_file.get_texts():
        output_file.write(' '.join(text) + '\n')
        count = count + 1
        if count % 10000 == 0:
            print('目前已处理%d条数据' % count)
    print('处理程序结束！')

    output_file.close()
    print('主程序结束！')