# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QidianPipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456lw',
            db = 'qidian',
            charset = 'utf8'
            )
        self.cur = self.client.cursor()
    def process_item(self, item, spider):
        sql = 'insert into qidian(bname,bauthor,btype,bstate,bimg,burl,bintro,bauturl) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        lis = (item['name'],item['author'],item['type'],item['state'],item['img'],item['url'],item['intro'],item['auturl'])
        self.cur.execute(sql,lis)
        self.client.commit()
        # self.cur.close()
        # self.client.close()
        return item
    def close_spider(self,spider):
        self.client.close()
    
