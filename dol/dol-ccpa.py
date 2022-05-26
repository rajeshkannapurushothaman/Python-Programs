import scrapy
import datetime
import time
import uuid
import re
from scrapy.utils.response import open_in_browser

class dolItems(scrapy.Item):
    ID = scrapy.Field()
    Product = scrapy.Field()
    ProductNumber = scrapy.Field()
    Title = scrapy.Field()
    description = scrapy.Field()
    Source_URL = scrapy.Field()
    Publish_Date = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    job_id = scrapy.Field()
    topices = scrapy.Field()

class DolSpider(scrapy.Spider):
    name = 'dol'
    start_urls = ['https://www.dol.gov/sites/dolgov/files/WHD/xml/opinionsCCPA.xml']

    def parse(self, response):
        cYear = datetime.datetime.now().year
        id = 0
        #for art in response.xpath('//number[contains(text(), '+ str(cYear) +')]/parent::opinion'):
        for art in response.xpath('//opinion'):
            id = id + 1
            items = dolItems()
            items['ProductNumber'] = art.xpath('number/text()').get()
            tmpTitle = art.xpath('title/text()').get().split('<br />')
            if len(tmpTitle) > 1:
                items['Title'] = tmpTitle[0].strip()
                items['description'] = re.sub('<([^><]+)>', '', tmpTitle[1]).strip()	
            else:
                items['Title'] = tmpTitle[0].strip()
                items['description'] = ""
            items['Source_URL'] = response.url
            items['Publish_Date'] = art.xpath('date/text()').get()
            items['Pdf_File_Name'] = ''
            items['Pdf_Source_URL'] = response.urljoin(art.xpath('pdf/text()').get())
            items['job_id'] = str(uuid.uuid4()) + '-' + str(int(time.time()))
            items['topices'] = art.xpath('topic/text()').get()
            items['Product'] = 'DOL'
            items['ID'] = str(id)
            yield items

        #open_in_browser(response)
