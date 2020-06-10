# -*- coding: utf-8 -*-
import scrapy


class SpiderTeatrosaopedroSpider(scrapy.Spider):
    name = 'spider_teatrosaopedro'
    allowed_domains = ['http://www.teatrosaopedro.com.br/eventos/']
    start_urls = ['http://http://www.teatrosaopedro.com.br/eventos//']

    def parse(self, response):
        pass
