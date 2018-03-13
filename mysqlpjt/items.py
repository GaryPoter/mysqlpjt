# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysqlpjtItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    real_name = scrapy.Field()
    time = scrapy.Field()
    area = scrapy.Field()
    type = scrapy.Field()
    language = scrapy.Field()
    sub = scrapy.Field()
    rating = scrapy.Field()
    duration = scrapy.Field()
    director = scrapy.Field()
    starting = scrapy.Field()
    abstract = scrapy.Field()
    download_url = scrapy.Field()
    image_url = scrapy.Field()
