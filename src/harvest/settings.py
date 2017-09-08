import os

BOT_NAME = 'harvest'
SPIDER_MODULES = ['harvest.spiders']
NEWSPIDER_MODULE = 'harvest.spiders'

DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS = 4
COOKIES_ENABLED = False

_src = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
_target = os.path.join(os.path.dirname(_src), 'target')
JOBDIR = os.path.join(_target, 'resume')
FEED_URI = os.path.join(_target, 'crawled')
FEED_FORMAT = 'csv'
