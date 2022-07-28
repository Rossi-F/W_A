import scrapy
from scrapy import Request
import re
from unidecode import unidecode

Manipulation_string = 'https://catalog.antiquorum.swiss/en/auctions/forte_dei_marmi_june_24_2022/lots?utf8=%E2%9C%93&amount_st=&amount_st=1&from_price=&to_price=&q=&goto='

class AntiquorumSpider(scrapy.Spider):
    name = "Antiquorum"
    start_urls = [Manipulation_string]
    Value = 1

    def parse(self, response):
        Lots = response.css('span#total_results::text').get()
        print('Number of Lots to be parsed -> ' + Lots)

        if (int(Lots) != 0):
            if (response.xpath('//*[@id="products"]/div[2]/div/div/span[2]').get() == None):
                self.Value += 1
                yield Request(Manipulation_string + str(self.Value))
            else:
                item = {
                    'Sell Price' : re.sub('[^A-Za-z0-9 -]+', '', unidecode(re.sub("[^0-9]", "", response.xpath('//*[@id="products"]/div[2]/div/div/span[2]').get()))),
                    'Brand' : re.sub('[^A-Za-z0-9 -]+', '', unidecode(re.sub("<.*?>", "", response.xpath('//*[. = "Brand"]/following-sibling::text()').get()))),
                    'Model' : re.sub('[^A-Za-z0-9 -]+', '', unidecode(re.sub("<.*?>", "", response.xpath('//*[. = "Model"]/following-sibling::text()').get()))),
                    'Reference' : re.sub('[^A-Za-z0-9 -]+', '', unidecode(re.sub("<.*?>", "", response.xpath('//*[. = "Reference"]/following-sibling::text()').get()))),
                    'Year' : re.sub('[^A-Za-z0-9 -]+', '', unidecode(re.sub("<.*?>", "", response.xpath('//*[. = "Year"]/following-sibling::text()').get()))),
                }
                yield item
                self.Value += 1
                yield Request(Manipulation_string + str(self.Value))