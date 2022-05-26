import scrapy
import datetime
import time
import uuid
from scrapy.utils.response import open_in_browser

class NrlbItems(scrapy.Item):
    ID = scrapy.Field()
    Source = scrapy.Field()
    Title = scrapy.Field()
    Source_URL = scrapy.Field()
    Publish_Date = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    job_id = scrapy.Field()
    CaseNumber = scrapy.Field()

class NrlbSpider(scrapy.Spider):
    name = 'nrlb'
    start_urls = ['https://www.nlrb.gov/guidance/memos-research/advice-memos/recently-released-advice-memos/']

    def parse(self, response):
        #open_in_browser(response)
        id = 0
        date_time = int(time.time())
        job_id = str(uuid.uuid4()) + '-' + str(date_time)
        for tr in response.xpath('//*[@id="recently_released_advice_memos"]/table[contains(@class, "case-decisions-table")]/tbody/tr'):
            caseNumber = tr.xpath('./td[1]/a/text()').get()
            caseTitle = tr.xpath('./td[2]/a/text()').get()
            PDF_Url = tr.xpath('./td[2]/a/@href').get()
            caseIssDate = tr.xpath('./td[3]/text()').get()
            caseRelDate = tr.xpath('./td[4]/text()').get()
            id = id + 1
            print(caseNumber,'--',caseTitle,'--',caseIssDate,'--',caseRelDate,'\n')
            items = NrlbItems()
            items['ID'] = id
            items['Source'] = 'NRLB'
            items['Title'] = caseTitle
            items['Source_URL'] = response.url
            items['CaseNumber'] = caseNumber
            items['Publish_Date'] = caseRelDate
            items['Pdf_File_Name'] = ''
            items['Pdf_Source_URL'] = PDF_Url
            items['job_id'] = job_id            
            yield items
            
            
