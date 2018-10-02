# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from qidian.items import QidianItem

class QdSpider(scrapy.Spider):
    name = 'qd'
    allowed_domains = ['www.qidian.com/all']
    start_url = 'https://www.qidian.com/all?page={page}'
    def start_requests(self):
        for page in range(1,51):
            yield Request(url=self.start_url.format(page=page),callback=self.parse)
    def parse(self, response):
        items = response.css('.all-book-list li')
        data = QidianItem()
        for item in items:
            data['name'] = item.css('.book-mid-info a::text').extract_first()
            data['author'] = item.css('.author a.name::text').extract_first()
            data['img'] = item.css('.book-img-box a img::attr(src)').extract_first()
            data['url'] = item.css('.book-img-box a::attr(href)').extract_first()
            data['state'] = item.css('.author span::text').extract_first()
            data['type'] = item.css('.author a.go-sub-type::text').extract_first()
            data['intro'] = item.css('.intro::text').extract_first().strip()
            data['auturl'] = item.css('.author a.name::attr(href)').extract_first()
            yield data
            
        
            
