import scrapy
from ..items import RottoVideoItem

class RottoSpider(scrapy.Spider):
    name = 'rotto'
    # allowed_domains = ['rotto.gov.in']
    start_urls = ['http://rottopgimer.in/web/videos/']

    def parse(self, response):
        items=RottoVideoItem()
        videos=response.css('td')

        for video in videos:
            url=video.css('iframe').css("::attr(src)").extract()
            items['videoLink']=url
            yield items

    
