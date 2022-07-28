import scrapy
import requests

class LoupeThisSpider(scrapy.Spider):
    name = "LoupeThis"
    start_urls = ['https://api.loupethis.com/api/v1/auctions?status=closed&sort_by=ends_at_desc&per_page=606']

    def parse(self, response):
        r = response.json()
        i = 0
        while (i != len(r['data'])):
            item = {
                'Brand/Description/Price': r['data'][i]['attributes']['title'],
                'Price': round((r['data'][i]['attributes']['current_bid_price_cents'] / 100) * 0.1 ) + (r['data'][i]['attributes']['current_bid_price_cents'] / 100),
                'WinningUserId': r['data'][i]['attributes']['winning_bid_user_id'],
            }
            yield item
            i+=1