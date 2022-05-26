# -*- coding: utf-8 -*-
import scrapy
from scrapy import item

class SupervisoryHighlightsItem(scrapy.Item):
    title = scrapy.Field()
    topics = scrapy.Field()
    pdfurl = scrapy.Field()

class SupervisoryHighlightsSpider(scrapy.Spider):
    name = 'supervisory-highlights'
    start_urls = ['https://www.consumerfinance.gov/compliance/supervisory-highlights/']

    def parse(self, response):
        try:
            if response.status == 200:
                title = response.xpath('//div[@class="m-info-unit_heading-text"]/h3/text()').get()
                topics = response.xpath('//div[@class="m-info-unit_content"]/p/text()').get()
                pdfURL = response.xpath('//div[@class="m-info-unit_content"]/ul/li/a/@href').get()

                if pdfURL != None and pdfURL != '':
                    item = SupervisoryHighlightsItem()
                    item['title'] = title
                    item['topics'] = topics
                    item['pdfurl'] = pdfURL
                    yield item
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)