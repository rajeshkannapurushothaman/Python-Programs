import scrapy
import datetime
import time
import uuid


class JusticeItems(scrapy.Item):
    ID = scrapy.Field()
    Source = scrapy.Field()
    Title = scrapy.Field()
    Source_URL = scrapy.Field()
    Publish_Date = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    job_id = scrapy.Field()
    CaseNumber = scrapy.Field()
    topices = scrapy.Field()
    PRnumber = scrapy.Field()

class JusticeSpider(scrapy.Spider):
    name = 'justice'
    allowed_domains = ['https://www.justice.gov/news/']
    start_urls = ['https://www.justice.gov/news/']

    def parse(self, response):
        for arturl in response.xpath('//section[@aria-label="Main section"]//div[@class="views-field views-field-title"]/span/a'):            
            req = scrapy.Request(response.urljoin(arturl.xpath('@href').get()), callback=self.JusticePage, dont_filter=True)
            yield req
    
    def JusticePage(self, response):
        items = JusticeItems()
        items['Source_URL'] = response.url
        items['Title'] = response.xpath('//article//*/h1[@id="node-title"]/text()').get()
        items['Publish_Date'] = response.xpath('//div[contains(@class, "field--name-field-pr-date")]/div/div/span/text()').get()
        items['topices'] = response.xpath('//div[contains(@class, "field--name-field-pr-topic")]/div[contains(text(), "Topic")]/following-sibling::div/div/text()').get()
        items['PRnumber'] = response.xpath('//div[contains(@class, "field--name-field-pr-number")]/div[contains(text(), "Press Release Number:")]/following-sibling::div/div/text()').get()
        fullContent = response.xpath('//div/div[@class="l-main"]/div[@role="main"]').get()
        yield items
        
        