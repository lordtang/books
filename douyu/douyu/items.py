# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片链接
    link = scrapy.Field()
    name = scrapy.Field()
    room = scrapy.Field()
    city = scrapy.Field()
