# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.qiushibaike.qiushibaike.items import QiushibaikeItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'  # 名字必须唯一
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        # selectorList
        divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in divs:
            # selector
            author = div.xpath('.//h2/text()').get().strip()
            content = div.xpath('.//div[@class="content"]//text()').getall()
            content = ",".join(content).strip()
            # duanzi = {
            #     'author': author,
            #     'content': content
            # }
            # yield duanzi
            item = QiushibaikeItem(author=author,content=content)
            yield item