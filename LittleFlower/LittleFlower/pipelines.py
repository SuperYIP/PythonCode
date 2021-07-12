# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class LittleflowerPipeline:
    def __init__(self):  # 参看文章：https://blog.csdn.net/loner_fang/article/details/81056191
        self.conn = pymysql.connect('127.0.0.1', 'root', 'yhdpxy5111', 'edu_spider', charset='utf8',
                                    use_unicode=True)  # 从前到后本地ip，用户名，密码，数据库名，后两项保证编码正确
        self.cursor = self.conn.cursor()  # 创建游标

    def process_item(self, item, spider):
        insert_sql = """insert into edu_data(title, date, url) VALUES (%s, %s, %s)"""  # 插入数据语句，jd_five为数据库中表名
        self.cursor.execute(insert_sql, (item['article_title'], item['article_date'], item['article_url']))  # 插入操作
        self.conn.commit()  # 提交，不进行提交无法保存到数据库

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()