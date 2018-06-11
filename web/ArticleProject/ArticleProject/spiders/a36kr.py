# -*- coding: utf-8 -*-
import json
import time

import scrapy
from urllib import parse

from ArticleProject.items import ArticleprojectItem


class A36krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['www.36kr.com']
    start_urls = ['http://www.36kr.com/']
    article_url = 'http://36kr.com/api/search-column/mainsite?'
    page = 1
    per_page = 20

    def random_timestamp(self):
        return str(round(int(time.time() * 1000)))

    def get_param(self):
        timestamp = self.random_timestamp()
        return {
            'per_page': self.per_page,
            'page': self.page,
            '_': timestamp
        }

    def start_requests(self):
        url = self.article_url + parse.urlencode(self.get_param())
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        results = json.loads(response.text)
        item = ArticleprojectItem()
        if 'data' in results:
            if 'items' in results.get('data'):
                items = results.get('data').get('items')
                for result in items:
                    for field in result.keys():
                        if field in item.fields:
                            item[field] = result.get(field)
                    yield item
            if 'total_count' in results.get('data'):
                self.page = self.page + 1
                if self.page <= results.get('data').get('total_count') // self.per_page + 1:
                    yield scrapy.Request(url=self.article_url + parse.urlencode(self.get_param()), callback=self.parse,
                                         dont_filter=True)
