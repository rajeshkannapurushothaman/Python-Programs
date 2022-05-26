# -*- coding: utf-8 -*-
import scrapy

class SupervisionExaminationsItem(scrapy.Item):
    pdfURL = scrapy.Field()
    title = scrapy.Field()
    published = scrapy.Field()

class SupervisionExaminationsSpider(scrapy.Spider):
    name = 'supervision-examinations'
    start_urls = ['https://www.consumerfinance.gov/compliance/supervision-examinations/']

    def parse(self, response):
        try:
            if response.status == 200:
                info = SupervisionExaminationsItem()
                info['pdfURL'] = response.urljoin(response.xpath('//div[@class="m-full-width-text"]/h3/following-sibling::p/a/@href').get())
                info['title'] = response.xpath('//div[@class="m-full-width-text"]/h3/following-sibling::p/a/span/text()').get()
                info['published'] = response.xpath('substring-after(//div[@class="m-full-width-text"]/h3/following-sibling::p, "Updated ")').get()
                yield info
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)