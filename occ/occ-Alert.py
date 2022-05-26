import scrapy
import datetime
import time
import uuid
import re
import json
from scrapy.utils.response import open_in_browser

class occBulletinItems(scrapy.Item):
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

class OccBulletinSpider(scrapy.Spider):
    name = 'occBulletin'
    start_urls = ['https://www.occ.gov/news-events/newsroom/index.html?nr=Bulletin']

    def parse(self, response):
        headers = {
            'Connection' : 'keep-alive',
            'sec-ch-ua' : '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'Accept' : 'application/json, text/plain, */*',
            'Content-Type' : 'application/json',
            'sec-ch-ua-mobile' : '?0',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform' : '"Windows"',
            'Origin' : 'https://www.occ.gov',
            'Sec-Fetch-Site' : 'same-site',
            'Sec-Fetch-Mode' : 'cors',
            'Sec-Fetch-Dest' : 'empty',
            'Referer' : 'https://www.occ.gov/',
            'Accept-Language' : 'en-US,en;q=0.9,ta;q=0.8'
        }
        
        data = '{"Keywords":[],"Topics":[],"NewsTypes":["Bulletin"],"EarliestPublishDateTime":null,"LatestPublishDateTime":null}'
        url = 'https://apps.occ.gov/Occ.DataServices.WebApi.Public/api/NewsItems/Site/516/Search/Options'
        response = scrapy.Request(url, headers=headers, body=data, method="POST", callback=self.jsonResult)
        yield response
    
    def jsonResult(self, response):
        if response.status == 200:
            alljson = json.loads(response.text)
            PublishDate = alljson[0]['PublishDate'].split('T')[0]
            id = 0
            for info in alljson:
                item = occBulletinItems()
                if info['PublishDate'].split('T')[0] == PublishDate:
                    id = id + 1
                    item['ProductNumber'] = info['ReleaseId']
                    item['Title'] = info['ContentTitle']
                    item['Publish_Date'] = info['PublishDate'].split('T')[0]
                    item['topices'] = ",".join(info['Topics'])
                    item['Source_URL'] = response.url
                    item['Pdf_Source_URL'] = info['Url']
                    item['Product'] = 'OCC'
                    item['ID'] = str(id)
                    item['job_id'] = str(uuid.uuid4()) + '-' + str(int(time.time()))
                    yield item
                    
                else:
                    break
               
                
