# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "Douyu"
    allowed_domains = ["douyucdn.com"]
    base_url = 'http://capi.douyucdn.cn/api/v1/live?limit=20&offset='
    offset = 0
    start_urls = (
        base_url + str(offset),
    )

    def parse(self, response):
        # r_list存放所有主播信息
        r_list = json.loads(response.text)['data']
        if not r_list:
            return

        for r in r_list:
            item = DouyuItem()
            item['link'] = r['vertical_src']
            item['name'] = r['nickname']
            item['room'] = r['room_id']
            item['city'] = r['anchor_city']

            yield item
        # 翻页
        self.offset += 20
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse,dont_filter=True)
