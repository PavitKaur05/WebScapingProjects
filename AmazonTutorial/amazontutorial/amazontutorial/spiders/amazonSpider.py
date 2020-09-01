import scrapy
from ..items import AmazontutorialItem

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonSpider'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/s?i=stripbooks&bbn=1402038031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1402038031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_binding_browse-bin%3A1318376031&dc&fst=as%3Aoff&qid=1598388800&rnid=1318374031&ref=sr_nr_p_n_binding_browse-bin_7']

    def parse(self, response):
        items=AmazontutorialItem()

        books=response.css('.s-latency-cf-section')
        for book in books:
            title=book.css('.a-color-base.a-text-normal').css('::text').extract_first()
            author=book.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract_first()
            price=book.css('.a-spacing-top-small .a-price-whole').css('::text').extract_first()

            if(title==None or author ==None or price==None):
                pass
            else:
                items['title']=title
                items['author']=author.strip()
                items['price']=price
                
                yield items

        next_page=response.css('.a-last a').css('::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        
