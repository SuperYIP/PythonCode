# -*- coding: utf-8 -*-
import scrapy
import re
import json
from ..items import SpiderJdcommentsItem    #这里注意，引用SpiderJdcommentsItem时用spider_JDComments.spider_JDComments.SpiderJdcommentsItem会报错

class JdSpiderSpider(scrapy.Spider):
    name = 'JD_spider'  #爬虫名
    # allowed_domains = ['list.jd.com']     #允许在此域名内爬取
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_commentcount_desc&trans=1&JL=6_0_0#J_main']  #起始爬取的url地址

    def parse(self, response):
        #爬取每个手机链接
        phone_url_list = response.xpath("//*[@id='J_goodsList']/ul/li")   #xpath解析获取手机链接列表
        for temp in phone_url_list:
            temp_url = "https:" + temp.xpath("./div/div[4]/a/@href").get()    #获取每个手机链接，这里的xpath是接着phone_url_list的写的，可以看到xpath前有个"."
            yield scrapy.Request(url=temp_url, callback=self.get_commenturl)  #将手机链接传给处理手机详情页的函数（在那里找到评论真实链接）

        #因为scrapy是异步爬取的，也就是说他有可能会先爬取页数靠后的手机信息，而页数靠后的手机信息评论少，所以我只让他爬前4页，每页60*10*80,四页也有一万多条，够用了
        for i in range(2,5):
            next_link = "https://list.jd.com/list.html?cat=9987,653,655&page=%s&sort=sort_commentcount_desc&trans=1&JL=6_0_0#J_main" % i
            yield scrapy.Request(next_link, callback=self.parse)

        # #获取下一页链接
        # next_link = response.xpath("//span[@class='p-num']//a[@class='pn-next']/@href").getall()
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request("https://list.jd.com/" + next_link, callback=self.parse)

    def get_commenturl(self, response):
        pattern = re.compile('\d+')  # 正则表达式匹配链接中的数字串，下面构造评论的url时会用到
        number = pattern.findall(response.url)[0]
        phone_name = response.xpath("//div[@class='itemInfo-wrap']/div[@class='sku-name']/text()").extract()   #获得手机名字
        phone_name = phone_name[0].strip()  #去除手机简评前后的空格
        for i in range(60):  # 获取每个手机的50页评论，因为京东只显示100页评论（虽然看着有10多万条）
            #好评信息，链接中score=3，中评2，差评1
            comment_url = "https://club.jd.com/comment/productPageComments.action?&productId=%s&score=3&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1" % (number, i)
            yield scrapy.Request(url=comment_url, meta = {'phone_name' : phone_name}, callback=self.detail)

    def detail(self, response):
        phone_name = response.meta['phone_name']
        data = json.loads(response.body.decode(response.encoding))  #response.body获得的是byte类型
                                                                    #scrapy中response.body 与 response.text区别：https://www.cnblogs.com/themost/p/8471953.html
                                                                    #对response的参数了解链接：https://blog.csdn.net/l1336037686/article/details/78536694
        if(data['comments']):   #判断评论信息是否存在，有的手机个别评论页数没有评论信息
            jdcomment_item = SpiderJdcommentsItem()  # 保存评论和星级数据所用
            for temp in data['comments']:
                if (temp['content'] and temp['score'] == 5 and phone_name):
                    jdcomment_item['phone_name'] = phone_name
                    jdcomment_item['comment'] = temp['content']
                    jdcomment_item['score'] = temp['score']
                    yield jdcomment_item
