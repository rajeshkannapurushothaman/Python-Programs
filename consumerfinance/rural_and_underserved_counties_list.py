# -*- coding: utf-8 -*-
import scrapy

class RuralAndUnderservedCountiesListItem(scrapy.Item):
    recentItem = scrapy.Field()
    title = scrapy.Field()
    pdfURL = scrapy.Field()

class RuralAndUnderservedCountiesListSpider(scrapy.Spider):
    name = 'rural-and-underserved-counties-list'
    start_urls = ['https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/rural-and-underserved-counties-list/']

    def parse(self, response):
        try:
            if response.status == 200:
                recentItem = response.xpath('//div[contains(@id, "final-lists-for-use-in-")]/h2/text()').get()
                for block in response.xpath('//div[contains(@id, "final-lists-for-use-in-")]/div/div'):
                    info = RuralAndUnderservedCountiesListItem()
                    info['title'] = block.xpath('./descendant::h3/text()').get()
                    info['pdfURL'] = response.urljoin(block.xpath("./descendant::a[contains(@href, '.pdf')]/@href").get())
                    info['recentItem'] = recentItem
                    yield info
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)