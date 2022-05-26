# -*- coding: utf-8 -*-
import scrapy

class PetitionsItem(scrapy.Item):
    published = scrapy.Field()
    title = scrapy.Field()
    urlPDF = scrapy.Field()

class PetitionsSpider(scrapy.Spider):
    name = 'petitions'
    start_urls = ['https://www.consumerfinance.gov/enforcement/petitions/']

    def parse(self, response):
        try:
            if response.status == 200:
                for artical in response.xpath('//article'):
                    info = {}
                    info['published'] = artical.xpath('./descendant::time[@class="datetime_date"]/text()').get()
                    info['title'] = artical.xpath('normalize-space(./div[@class="o-post-preview_content"]/h3/a/text())').get()
                    info['url'] = response.urljoin(artical.xpath('./div[@class="o-post-preview_content"]/h3/a/@href').get())
                    req = scrapy.Request(info['url'], method='GET', callback=self.itempage)
                    req.meta['info'] = info
                    yield req
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)

    def itempage(self, response):
        try:
            if response.status == 200:
                info = response.meta.get("info")
                pdfURLs = response.xpath('//div[@class="o-full-width-text-group"]/descendant::a[@class="a-link a-link__icon" and contains(@href, ".pdf")]/@href').getall()
                if len(pdfURLs) > 0:
                    for purl in pdfURLs:
                        item = PetitionsItem()
                        item['published'] = info['published']
                        item['title'] = info['title']
                        item['urlPDF'] = response.urljoin(purl)
                        yield item
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)