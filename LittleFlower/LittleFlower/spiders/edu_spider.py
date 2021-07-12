# -*- coding: utf-8 -*-
import scrapy
from ..items import LittleflowerItem

class EduSpider(scrapy.Spider):
    name = 'edu_spider'  #爬虫名
    # allowed_domains = ['list.jd.com']     #允许在此域名内爬取
    start_urls = ['http://edu.people.com.cn/GB/427940/index1.html']  #起始爬取的url地址

    def parse(self, response):
        #爬取每个新闻链接
        temp_url_list = response.xpath('//div[@class="ej_list_box clear"]/ul/li/a/@href').extract()   #xpath解析获取文章链接列表(url链接有缺失)
        #extract()方法提取出selector中的元素，response.xpath返回的类型是scrapy.selector.unified.Selector

        # 爬取每个新闻标题
        aritcle_title_list = response.xpath('//div[@class="ej_list_box clear"]/ul/li/a/text()').extract()

        # 爬取每个新闻发表时间
        article_date_list = response.xpath('//div[@class="ej_list_box clear"]/ul/li/em/text()').extract()


        #传递爬取的数据
        for temp_url, temp_title, temp_date in zip(temp_url_list, aritcle_title_list, article_date_list):
            edu_data_item = LittleflowerItem()
            edu_data_item['article_url'] = 'http://edu.people.com.cn' + temp_url #构造文章url
            edu_data_item['article_title'] = temp_title
            edu_data_item['article_date'] = temp_date
            yield edu_data_item

        # #因为scrapy是异步爬取的，也就是说他有可能会先爬取页数靠后的手机信息，而页数靠后的手机信息评论少，所以我只让他爬前4页，每页60*10*80,四页也有一万多条，够用了
        for i in range(1,13):
            next_link = 'http://edu.people.com.cn/GB/427940/index%s.html' %i
            yield scrapy.Request(next_link, callback=self.parse)




    # def detail(self, response):
    #     phone_name = response.meta['phone_name']
    #     data = json.loads(response.body.decode(response.encoding))  #response.body获得的是byte类型
    #                                                                 #scrapy中response.body 与 response.text区别：https://www.cnblogs.com/themost/p/8471953.html
    #                                                                 #对response的参数了解链接：https://blog.csdn.net/l1336037686/article/details/78536694
    #     if(data['comments']):   #判断评论信息是否存在，有的手机个别评论页数没有评论信息
    #         jdcomment_item = LittleflowerItem()  # 保存评论和星级数据所用
    #         for temp in data['comments']:
    #             if (temp['content'] and temp['score'] == 5 and phone_name):
    #                 jdcomment_item['phone_name'] = phone_name
    #                 jdcomment_item['comment'] = temp['content']
    #                 jdcomment_item['score'] = temp['score']
    #                 yield jdcomment_item
