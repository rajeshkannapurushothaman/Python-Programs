import scrapy
import datetime
import time
import uuid
from scrapy.utils.response import open_in_browser

class GaoItems(scrapy.Item):
    ID = scrapy.Field()
    Product = scrapy.Field()
    Title = scrapy.Field()
    Source_URL = scrapy.Field()
    Publish_Date = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    job_id = scrapy.Field()
    topices = scrapy.Field()

class GaoSpider(scrapy.Spider):
    name = 'gao'
    start_urls = ['https://www.gao.gov/reports-testimonies']

    def parse(self,response):
        #open_in_browser(response)
        source = "GAO"
        id = 0
        date_time = int(time.time())
        job_id = str(uuid.uuid4()) + '-' + str(date_time)

        for art in response.xpath('//article'):
            artTitle = art.xpath('./header//h4[@class="heading"]/a/text()').get()
            prodNum = art.xpath('./header//div[@class="product-number"]/div/text()').get()
            pubdate = art.xpath('./header//div[@class="dates"]/div[contains(text(),"Published:")]/text()').get()
            arturl = response.urljoin(art.xpath('./header//h4[@class="heading"]/a/@href').get())
            id = id + 1

            caseMeta = {"id":str(id),
                        "date_time":pubdate.replace('Published: ', ''),
                        "job_id":job_id,
                        "artTitle" : artTitle,
                        "prodNum" : prodNum}

            req = scrapy.Request(arturl, callback=self.billPage)
            req.meta['info']=caseMeta
            yield req
            # break

    def billPage(self, response):

        info = response.meta.get('info')
        pdfLinks = response.xpath('//div[@class="field__item"]/figure/a/div[contains(text(), "Full Report") or contains(text(), "Accessible")]/parent::a/@href').getall()
        topices = response.xpath('//div[@class="views-field views-field-field-topic"]/div/a/text()').get()
        if len(pdfLinks) > 0:
            for pdfLink in pdfLinks:
                items = GaoItems()
                items['ID'] = info['id']
                items['Product'] = "GAO"
                items['Title'] = info['artTitle']
                items['Source_URL'] = response.url
                items['Publish_Date'] = info['date_time']
                items['Pdf_File_Name'] = ''
                items['Pdf_Source_URL'] = 'https://www.gao.gov' + pdfLink.replace('/./', '/')
                items['job_id'] = info['job_id']
                items['topices'] = topices
                yield items