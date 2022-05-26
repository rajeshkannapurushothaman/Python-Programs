# -*- coding: utf-8 -*-
import scrapy
class CivilPenaltyFundItem(scrapy.Spider):
    title = scrapy.Field()
    pdfURL = scrapy.Field()

class CivilPenaltyFundSpider(scrapy.Spider):
    name = 'civil-penalty-fund'
    start_urls = ['https://www.consumerfinance.gov/enforcement/payments-harmed-consumers/civil-penalty-fund/']

    def parse(self, response):
        try:
            if response.status == 200:
                item = CivilPenaltyFundItem()
                item['pdfURL'] = response.urljoin(response.xpath('//span[contains(text(), "in one document")]/parent::a/@href').get())
                item['title'] = response.xpath('//span[contains(text(), "in one document")]/text()').get()
                yield item
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)