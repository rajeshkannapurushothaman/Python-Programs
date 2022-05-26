# -*- coding: utf-8 -*-
import scrapy
import re
class FundsTransferRequestsItem(scrapy.Item):
    title = scrapy.Field()
    publishDate = scrapy.Field()
    pdfURL = scrapy.Field()

class FundsTransferRequestsSpider(scrapy.Spider):
    name = 'funds-transfer-requests'
    start_urls = ['https://www.consumerfinance.gov/about-us/budget-strategy/funds-transfer-requests/']

    def parse(self, response):
        try:
            if response.status == 200:
                i = 0
                for liEle in response.xpath('//div[@class="m-full-width-text"]/ul[1]/li'):
                    pdfURL = response.urljoin(liEle.xpath('./a/@href').get())
                    tmpStr = liEle.xpath('./a/span/text()').get()
                    m = re.search('^((([A-z]+) ([0-9]+), ([0-9]{4})), )', tmpStr)
                    if m:
                        publishDate = m.group(2)
                        title = tmpStr.replace(m.group(1), '').strip()
                        item = FundsTransferRequestsItem()

                        item['title'] = title
                        item['publishDate'] = publishDate
                        item['pdfURL'] = pdfURL
                        yield item
                    i = i + 1
                    if i == 5:
                        break
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)