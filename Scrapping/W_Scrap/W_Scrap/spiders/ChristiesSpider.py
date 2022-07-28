import scrapy

class ChristiesSpider(scrapy.Spider):
    name = "Christies"
    start_urls = ['https://onlineonly.christies.com/s/watches-online-new-york-edit/lots/2122?filters=&loadall=true&page=2&searchphrase=&sortby=HighEstimateHighToLow&themes=']

    def parse(self, response):
        print(response.xpath('/html/body/div[1]/chr-auction-results-view//*[@id="main-content"]').get())
        for products in response.xpath('/html/body/div[1]/chr-auction-results-view > //*[@id="main-content"]/section/div/ul/li[1]'):
            try:
                yield {
                        'Sell Price': 'Not for Now',
                        'Reference': products.css('span.chr-lot-tile__number').get(),
                        'Model': 'Not for Now',
                        'Brand': products.css('span.chr-lot-tile__secondary-price-value').get(),
                    }
            except:
                print('PARSING ERROR')