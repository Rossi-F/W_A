import scrapy
import re
from unidecode import unidecode


class PhillipsSpider(scrapy.Spider):
    name = "Phillips"
    start_urls = ['https://www.phillips.com/auctions/auction/HK080122']

    def parse(self, response):
        for products in response.xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/ul/li'):
            item = {
                'Brand' : products.xpath('.//*[@class="phillips-lot__description__artist"]').get(),
                'Reference' : products.xpath('.//*[contains(text(), "Ref.")]').get(),
                'Model': products.xpath('.//*[contains(text(), "Model:")]').get(),
                'Price': products.xpath('.//*[@class="phillips-lot__sold"]').get(),
            }
            if (item['Brand'] != None):
                item['Brand'] = unidecode(re.sub('<[^<]+?>', '', item['Brand']))
            if (item['Reference'] != None):
                item['Reference'] = unidecode(re.sub('<[^<]+?>', '', item['Reference']))
            if (item['Model'] != None):
                item['Model'] = unidecode(re.sub('<[^<]+?>', '', item['Model']).strip("Model:").strip("\xa0"))
            if (item['Price'] != None):
                item['Price'] = unidecode(re.sub('<[^<]+?>', '', item['Price'])).strip("Sold for  ")
            yield item

            
