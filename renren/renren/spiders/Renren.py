# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'Renren'
    allowed_domains = ['renren.com']

    # start_urls = ['http://www.renren.com/']
    def start_requests(self):
        url = "http://www.renren.com/PLogindo"
        yield scrapy.FormRequest(url=url,
                                 formdata={"email": "17602823158", "password": "rr147896"},
                                 callback=self.parseHtml
                                 )

    def parseHtml(self, response):
        with open("liang.html", 'w') as f:
            f.write(response.text)
            print('成功' + '*' * 100)


    def parse(self, response):
        print(response.text)
