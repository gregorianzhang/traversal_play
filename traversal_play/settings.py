# Scrapy settings for traversal_play project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'traversal_play'

SPIDER_MODULES = ['traversal_play.spiders']
NEWSPIDER_MODULE = 'traversal_play.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'traversal_play (+http://www.yourdomain.com)'


LOG_LEVEL = 'DEBUG'

ITEM_PIPELINES = {
        'traversal_play.pipelines.MysqlPipeline': 888,
}

