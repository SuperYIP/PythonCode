from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
import jieba                   	 #jieba分词

path_txt = r'F:\t\test\2.txt'
f = open(path_txt,'r',encoding='UTF-8').read()
# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(f))	#cut_text类型为str
#生成词云
wordcloud = WordCloud(
   #设置字体，不然会出现乱码，文字的路径是电脑的字体一般路径，可以换成别的
   font_path="C:/Windows/Fonts/simfang.ttf",
   #设置背景，宽、高
   background_color="white",width=1000,height=880).generate(cut_text)   #生成词云
# wordcloud.to_file(r'F:\t\test\1.jpg')  #保存词云图片
#将词云显示在屏幕上
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")	#隐藏坐标轴
plt.show()

