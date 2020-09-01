import scrapy
from ..items import GooglenewsItem

class NewsspiderSpider(scrapy.Spider):
    name = 'newsSpider'
    # allowed_domains = ['googlenews']

    def __init__(self,keyword='',**kwargs):
        # super(NewsspiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://news.google.com/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN%3Aen']
        super().__init__(**kwargs)

    def parse(self, response):
        newsArticles=response.css('.NiLAwe')
        items=GooglenewsItem()
        # print(len(newsArticles))
        for article in newsArticles:
            articleTitle=article.css('.DY5T1d').css('::text').extract()
            articleLink=article.css('.DY5T1d').css('::attr(href)').extract()
            items['articleTitle']=articleTitle
            items['articleLink']='https://news.google.com/'+articleLink[0]
            yield items
