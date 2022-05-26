# -*- coding: utf-8 -*-
import scrapy

class BlogItem(scrapy.Item):
    categoryName = scrapy.Field()
    published = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    urlHTML = scrapy.Field()
    urlPDF = scrapy.Field()
    topics = scrapy.Field()

class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = ['https://www.consumerfinance.gov/about-us/blog/']

    def parse(self, response):
        try:
            if response.status == 200:
                for artical in response.xpath('//article'):
                    info = {}
                    info['categoryName'] = artical.xpath('normalize-space(./descendant::span[@class="m-meta-header_category"]/text()[last()])').get()
                    info['published'] = artical.xpath('./descendant::time[@class="datetime_date"]/text()').get()
                    info['title'] = artical.xpath('normalize-space(./div[@class="o-post-preview_content"]/h3/a/text())').get()
                    info['url'] = artical.xpath('./div[@class="o-post-preview_content"]/h3/a/@href').get()
                    info['description'] = artical.xpath('./descendant::div[@class="o-post-preview_description"]/p/text()').get()
                    topics = []
                    for liEle in artical.xpath('./div/div[@class="tags tags__hide-heading"]/ul/li'):
                        tmp = liEle.xpath('normalize-space(./a/text()[last()])').get()
                        if tmp != None and tmp != '':
                            topics.append(tmp)
                    info['topics'] = ','.join(topics)
                    req = scrapy.Request(response.urljoin(info['url']), method='GET', callback=self.itempage)
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
                        item = BlogItem()
                        item['categoryName'] = info['categoryName']
                        item['published'] = info['published']
                        item['title'] = info['title']
                        item['description'] = info['description']
                        item['urlHTML'] = response.url
                        item['urlPDF'] = purl
                        item['topics'] = info['topics']
                        yield item

                else:
                    item = BlogItem()
                    item['categoryName'] = info['categoryName']
                    item['published'] = info['published']
                    item['title'] = info['title']
                    item['description'] = info['description']
                    item['urlHTML'] = response.url
                    item['urlPDF'] = ''
                    item['topics'] = info['topics']
                    yield item
            else:
                print('request failed for the url is ' + response.url)
        except Exception as Err:
            print(Err)