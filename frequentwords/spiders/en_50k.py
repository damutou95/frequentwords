# -*- coding: utf-8 -*-
import scrapy
from frequentwords.items import FrequentwordsItem
from scrapy import Request
from frequentwords import settings
class En50kSpider(scrapy.Spider):
    name = 'en_50k'
    #allowed_domains = ['sss']
    start_urls = ['https://github.com/hermitdave/FrequencyWords/blob/master/content/2016/en/en_50k.txt']
    headers = settings.HEADERS
    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.parse, headers = self.headers)

    def parse(self, response):
        words = response.xpath('//tbody/tr')
        for word in words:
            item = FrequentwordsItem()
            temp = word.xpath('./td[@class="blob-code blob-code-inner js-file-line"]/text()').extract_first().split(' ')
            item['word'] = temp[0]
            item['rate'] = temp[1]
            return item
