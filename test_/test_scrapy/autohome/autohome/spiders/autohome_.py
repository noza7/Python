# -*- coding: utf-8 -*-
import scrapy


class AutohomeSpider(scrapy.Spider):
    name = 'autohome_'
    allowed_domains = ['www.autohome.com.cn']
    start_urls = ['http://www.autohome.com.cn/']

    def parse(self, response):
        pass
