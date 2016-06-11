import scrapy

class YoupUserComment(scrapy.Item):
    name = scrapy.Field()
    text = scrapy.Field()
