# -*- coding: utf-8 -*-
import scrapy

class TestimonyItem(scrapy.Item):
    categoryName = scrapy.Field()
    published = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()

class TestimonySpider(scrapy.Spider):
    name = 'testimony'
    start_urls = ['https://www.consumerfinance.gov/about-us/newsroom/?title=&categories=testimony&from_date=&to_date=']

    def parse(self, response):
        try:
            if response.status == 200:
                for artical in response.xpath('//article'):
                    info = {}
                    info['categoryName'] = artical.xpath('normalize-space(./descendant::span[@class="m-meta-header_category"]/text()[last()])').get()
                    info['published'] = artical.xpath('./descendant::time[@class="datetime_date"]/text()').get()
                    info['title'] = artical.xpath('normalize-space(./div[@class="o-post-preview_content"]/h3/a/text())').get()
                    url = artical.xpath('./div[@class="o-post-preview_content"]/h3/a/@href').get()
                    info['description'] = artical.xpath('./descendant::div[@class="o-post-preview_description"]/p/text()').get()
                    info['url'] = response.urljoin(url)
                    yield info
            else:
                print('request failed for the url is ' + response.url)

        except Exception as Err:
            print(Err)