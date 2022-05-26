# -*- coding: utf-8 -*-
import scrapy
import re

class InstitutionsItem(scrapy.Item):
    pdfURL = scrapy.Field()
    publishdate = scrapy.Field()

class InstitutionsSpider(scrapy.Spider):
    name = 'institutions'
    start_urls = ['https://www.consumerfinance.gov/compliance/supervision-examinations/institutions/']

    def parse(self, response):
        try:
            if response.status == 200:
                pdfURL = response.urljoin(response.xpath('//span[contains(text(), "Current list PDF")]/parent::a/@href').get())
                tmptxt = response.xpath('//span[contains(text(), "Current list PDF")]/ancestor::p/preceding-sibling::p[1]/text()').get()
                publishdate = ''
                m = re.search('(([A-z]+) ([0-9]+), ([0-9]{4}))', tmptxt)
                if m:
                    publishdate = m.group(1)

                item = InstitutionsItem()
                item['pdfURL'] = pdfURL
                item['publishdate'] = publishdate
                yield item
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)