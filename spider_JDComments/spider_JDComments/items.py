# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderJdcommentsItem(scrapy.Item):
    # define the fields for your item here like:
    comment = scrapy.Field()    #评论评论
    score = scrapy.Field()   #评论星级
    phone_name = scrapy.Field()  #手机名称