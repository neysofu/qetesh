import bs4
import scrapy
from harvest.items import YoupUserComment

class YoupCollector(scrapy.spiders.CrawlSpider):

    __home__ = 'http://www.youporn.com'
    __ajax__ = __home__ + '/ajax/video/comments/'

    name = 'youp'
    allowed_domains = [__home__]
    start_urls = [__home__ + '/most_discussed/all/']

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        for item in self.items(soup):
            yield item
        yield self.nextPage(soup)

    def items(self, soup):
        for tag in soup.findAll('div', {'class':'video-box four-column'}):
            url = YoupCollector.__ajax__ + tag['data-video-id'] + '/'
            yield scrapy.Request(url, self.parseItem, dont_filter=True)

    def parseItem(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        for tag in soup.findAll('li', {'class':'comment'}):
            yield self.parseElement(tag)

    def parseElement(self, tag):
        tag.span.decompose()
        msg = YoupUserComment()
        msg['name'] = tag.find('p', {'class':'name'}).text
        msg['text'] = tag.find('p', {'class':'message'}).text
        return msg

    def nextPage(self, soup):
        url = soup.find('div', {'class':'prev-next'}).find('a')['href']
        return scrapy.Request(url, callback=self.parse)
