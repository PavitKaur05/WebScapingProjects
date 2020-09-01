import scrapy
from ..items import QuotestutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls=['http://quotes.toscrape.com/login']

    def parse(self,response):
        token=response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'pavit',
            'password':'123'
        },callback=self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
        item=QuotestutorialItem()
        all_div_quotes=response.css('div.quote')
        for quote in all_div_quotes:
            quoteText=quote.css('span.text::text').extract()
            author=quote.css('.author::text').extract()
            tags=quote.css('.tag::text').extract()

            item['title']=quoteText
            item['author']=author
            item['tags']=tags
            yield item # everytime a instance of item container is yelded it passes to pipeline

        # next_page=response.css('.next a::attr(href)').get()

        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.start_scraping)
            
