# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from mysqlpjt.sql_utils import get_insert_statement

class MysqlpjtPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mypydb')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if item["movie_name"] is None:
            return item

        movie_name = item["movie_name"]
        real_name = item["real_name"]
        time = item["time"]
        area = item["area"]
        type = item["type"]
        language = item["language"]
        sub = item["sub"]
        rating = item["rating"]
        duration = item["duration"]
        director = item["director"]
        starting = item["starting"]
        abstract = item["abstract"]
        download_url = item["download_url"]
        image_url = item["image_url"]
        propertys = [movie_name, real_name, time, area,
                    type, language, sub, rating,
                    duration, director, starting, abstract,
                    download_url, image_url]
        sql = "insert into movie (movie_name, real_name, time, area, type," \
              "language, sub, rating, duration, director," \
              "star, abstract, download_url, image_url) VALUES ('" + "','".join(propertys) + "')"
        print(sql)
        # self.conn.query(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):

        self.conn.close()
