import scrapy

class BotUserComment(scrapy.Item):
    name = scrapy.Field()
    text = scrapy.Field()
