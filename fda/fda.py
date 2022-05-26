import scrapy
import datetime
import time
import uuid
import re
import json
from urllib.parse import urljoin

class fdaItems(scrapy.Item):
    ID = scrapy.Field()
    job_id = scrapy.Field()
    Product = scrapy.Field()
    ProductNumber = scrapy.Field()
    Summary = scrapy.Field()
    Organization = scrapy.Field()
    Source_URL = scrapy.Field()
    IssueDate = scrapy.Field()
    Pdf_File_Name = scrapy.Field()
    Pdf_Source_URL = scrapy.Field()
    Topices = scrapy.Field()
    Status = scrapy.Field()

class fdaSpider(scrapy.Spider):
    name = 'fda'
    start_urls = ['https://www.fda.gov/files/api/datatables/static/search-for-guidance.json']

    def parse(self, response):
        if response.status == 200:
            alljson = json.loads(response.text)
            id = 0
            last_month = datetime.datetime.now() - datetime.timedelta(days=30)            
            for doc in alljson:
                if doc['field_issue_datetime'] != "" and datetime.datetime.strptime(doc['field_issue_datetime'], '%m/%d/%Y') > last_month:
                    id = id + 1
                    item = fdaItems()
                    item['Product'] = "FDA"
                    item['ProductNumber'] = re.sub("<[^><]+>","",doc['field_docket_number'])
                    item['Summary'] = re.sub("<[^><]+>","",doc['title'])
                    item['Topices'] = doc['topics-product']
                    item['IssueDate'] = doc['field_issue_datetime']
                    item['Organization'] = doc['field_issuing_office_taxonomy']
                    item['Status'] = doc['field_final_guidance_1']
                    item['Source_URL'] = 'https://www.fda.gov/regulatory-information/search-fda-guidance-documents'
                    item['ID'] = str(id)
                    temp = doc['field_associated_media_2']
                    m = re.search('<a href="([^\"]+)">', temp)
                    if m:
                        item['Pdf_Source_URL'] = urljoin('https://www.fda.gov/', m.group(1))
                    item['job_id'] = str(uuid.uuid4()) + '-' + str(int(time.time()))
                    yield item
