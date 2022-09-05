import scrapy
import re
from unidecode import unidecode


class PhillipsSpider(scrapy.Spider):
    name = "Phillips"
    start_urls = ['https://www.phillips.com/auctions/auction/HK080322']

    def parse(self, response):
        for products in response.xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/ul/li'):
            temp = {
                'Brand' : products.xpath('.//*[@class="phillips-lot__description__artist"]').get(),
                'Reference' : products.xpath('.//*[contains(text(), "Ref.")]').get(),
                'Model': products.xpath('.//*[contains(text(), "Model:")]').get(),
                'P': products.xpath('.//*[@class="phillips-lot__sold"]').get(),
                'B-D' : None,
            }

            item ={}

            if (temp['Brand'] != None):
                temp['Brand'] = unidecode(re.sub('<[^<]+?>', '', temp['Brand']))
                temp['B-D'] = temp['Brand'] + ' '
            if (temp['Model'] != None):
                temp['Model'] = unidecode(re.sub('<[^<]+?>', '', temp['Model']).strip("Model:").strip("\xa0"))
                temp['B-D'] += temp['Model'] + ' '
            if (temp['Reference'] != None):
                temp['Reference'] = unidecode(re.sub('<[^<]+?>', '', temp['Reference']))
                temp['B-D'] += temp['Reference']
            if (temp['P'] != None):
                temp['P'] = unidecode(re.sub('<[^<]+?>', '', temp['P'])).strip("Sold for  ")

            if (temp['B-D'] != None):
                item['B-D'] = temp['B-D']
            if (temp['P'] != None):
                item['P'] = (temp['P'].replace(",", ""))

            yield item

## Rewrite with integration of simple two columns, "B-D" and "Price" (B-D being brand followed by model and reference)
