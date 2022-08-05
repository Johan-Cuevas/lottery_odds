import scrapy


class QuotesSpider(scrapy.Spider):
    name = "lottery"
    start_urls = [
        "https://www.calottery.com/draw-games/powerball#section-content-1-3"
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)




        