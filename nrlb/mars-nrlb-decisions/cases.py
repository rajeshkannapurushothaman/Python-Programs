import scrapy
import datetime
import time
import uuid
from scrapy.utils.response import open_in_browser

class CasesItems(scrapy.Item):
    ID = scrapy.Field()
    Source = scrapy.Field()
    Title = scrapy.Field()
    Source_URL = scrapy.Field()
    Publish_Date = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    job_id = scrapy.Field()
    CaseNumber = scrapy.Field()

class CasesSpider(scrapy.Spider):
    name = 'cases'
    start_urls = ['https://www.nlrb.gov/cases-decisions/decisions/board-decisions/']

    def parse(self, response):
        pass
