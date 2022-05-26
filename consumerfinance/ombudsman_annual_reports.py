# -*- coding: utf-8 -*-
import scrapy
from scrapy import item

class OmbudsmanAnnualReportsItem(scrapy.Item):
    title = scrapy.Field()
    pdfURL  = scrapy.Field()

class OmbudsmanAnnualReportsSpider(scrapy.Spider):
    name = 'ombudsman-annual-reports'
    start_urls = ['https://www.consumerfinance.gov/cfpb-ombudsman/ombudsman-annual-reports/']

    def parse(self, response):
        try:
            if response.status == 200:
                for liEle in response.xpath('//div[@class="o-info-unit-group"]/descendant::div[@class="m-info-unit"][1]/div[@class="m-info-unit_content"]/descendant::li'):
                    item = OmbudsmanAnnualReportsItem()
                    item['title'] = liEle.xpath('./a/span/text()').get()
                    item['pdfURL'] = liEle.xpath('./a/@href').get()
                    yield item
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)