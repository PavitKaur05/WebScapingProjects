# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OrgandonationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imageCaption=scrapy.Field()
    imageLink=scrapy.Field()


class RottoVideoItem(scrapy.Item):
    videoLink=scrapy.Field()

class NottoVideoItem(scrapy.Item):
    videoCaption=scrapy.Field()
    videoLink=scrapy.Field()


