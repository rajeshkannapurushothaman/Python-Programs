import scrapy
import datetime
import uuid
#from scrapy.utils.response import open_in_browser

class GaoItems(scrapy.Item):
    ID = scrapy.Field()
    Product = scrapy.Field()
    Title = scrapy.Field()
    Source_URL = scrapy.Field()
    Publish_Date = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    job_id = scrapy.Field()

class GaoSpider(scrapy.Spider):
    name = 'gao'
    start_urls = (
        'https://www.gao.gov/reports-testimonies',
        )
    def parse(self, response):
        yield scrapy.Request('https://www.gao.gov/reports-testimonies', method='GET', callback=self.parse1)

    def parse1(self,response):
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
            req = scrapy.Request(arturl, callback=self.parse2, meta={"source":source, "id":str(id), "date_time":pubdate, 'job_id':job_id})
            print(artTitle,'\n',prodNum,'\n',pubdate,'\n',arturl,'\n')
            
    def parse2(self,response):
