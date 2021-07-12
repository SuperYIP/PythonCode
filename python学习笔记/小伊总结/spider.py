# -*- coding:utf-8 -*-

import requests
import json
import time
import random
import xlwt
##爬取的手机是苹果11，网址为 https://item.jd.com/100008348542.html
    #好评
    #url = 'https://club.jd.com/comment/productPageComments.action?&productId=100008348542&score=3&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'%page

    #中评
    #url = 'https://club.jd.com/comment/productPageComments.action?&productId=100008348542&score=2&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'%page

    #差评
    #url = 'https://club.jd.com/comment/productPageComments.action?&productId=100008348542&score=1&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'%page

# 创建excell保存数据
file = xlwt.Workbook(encoding='utf-8')
sheet = file.add_sheet('data', cell_overwrite_ok=True)

for i in range(105):    #for循环遍历，批量爬取评论信息
    try:
        #构造url，通过在网页不断点击下一页发现，url中只有page后数字随页数变化，批量遍历就是根据这个
        #url去掉了callback部分，因为这部分内没有有用数据，并且不去掉后面转换为json格式会有问题
        url = 'https://club.jd.com/comment/productPageComments.action?&productId=100008348542&score=3&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % i
        #构造headers
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'referer': 'https://item.jd.com/100008348542.html'
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)  # 字符串转换为json数据
        page = i * 10   #这里是存储在excell中用到的，因为每爬取一个url会有10条评论，占excell 10列
        if(data['comments']):
            for temp in data['comments']:
                sheet.write(page, 0, page)  #序号
                sheet.write(page, 1, temp['content'])   #评论
                sheet.write(page, 2, temp['score']) #用户打的星级
                page = page + 1
            print('第%s页爬取成功' % i)
        else:
            print('.............第%s页爬取失败' %i)
            file.save('F:\\学习相关\\大四上\\毕设\\数据\\好评.xlsx') #保存到本地

    except Exception as e:
        print('爬取失败，url：%s'%url)
        print('page是%s'%i)
        continue
    time.sleep(random.random() * 5) #每循环一次，随机时间暂停再爬
file.save('F:\\学习相关\\大四上\\毕设\\数据\\t.xlsx')