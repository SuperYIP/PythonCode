# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LittleflowerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_title = scrapy.Field()  # 新闻标题
    article_date = scrapy.Field()  # 新闻发表时间
    article_url = scrapy.Field()  # 新闻详情页链接
