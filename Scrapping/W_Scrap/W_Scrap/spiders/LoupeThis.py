import scrapy
import json

class LoupeThisSpider(scrapy.Spider):
    name = "LoupeThis"
    start_urls = ['https://api.loupethis.com/api/v1/auctions?status=closed&sort_by=ends_at_desc&per_page=1000']

    def parse(self, response):
        r = json.loads(response.body)
        i = 0
        while (i != len(r['data'])):
            item = {
                'B-D': r['data'][i]['attributes']['title'],
                'P': round((r['data'][i]['attributes']['current_bid_price_cents'] / 100) * 0.1 ) + (r['data'][i]['attributes']['current_bid_price_cents'] / 100),
            }
            yield item
            i+=1