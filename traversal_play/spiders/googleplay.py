from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
import re
from traversal_play.items import TraversalPlayItem
from md5 import md5

class GoogleplaySpider(Spider):
    name = "googleplay"
    allowed_domains = ["play.google.com"]
    start_urls = (
        'https://play.google.com/store/apps/category/TOOLS/collection/topselling_free?start=0&num=24',
        )
    global category1
    global url1 
    category1 = 'TOOLS'
    url1 = 'https://play.google.com'

    def parse(self, response):
        if re.match(".*play\.google\.com.*",response.url):
            for pagenum in range(0,48,24):
                url = re.sub(r"start=\d+","start="+str(pagenum),response.url)
                yield Request(url, callback=self.parse_url)


    def parse_url(self, response):
	sel = Selector(response)
	appurls = ""
	appurls = sel.xpath('//*[@class="title"]/@href').extract()
        for url in appurls:
	    yield Request(url1 + url, callback=self.parse_app)


    def parse_app(self, response):
	print "------------------------------------------------------"
	print response.url
	items = []
	sel = Selector(response)
	i = TraversalPlayItem()
	i['url'] = response.url
	i['md5'] = md5(response.url).hexdigest()
	i['name'] = sel.xpath('//*[@class="document-title"]/div/text()').extract()
	i['devid'] = sel.xpath('//*[@itemprop="author"]/meta/@content').extract()
	i['icon'] = sel.xpath('//*[@class="cover-container"]/img/@src').extract()
	i['images'] = sel.xpath('//*[@class="screenshot"]/@src').extract()
	i['category'] = category1
	i['whatsnew'] = sel.xpath('//*[@class="recent-change"]/text()').extract()
	i['datepublished'] = sel.xpath('//*[@itemprop="datePublished"]/text()').extract()
	i['filesize'] = sel.xpath('//*[@itemprop="fileSize"]/text()').extract()
	i['numdownload'] = sel.xpath('//*[@itemprop="numDownloads"]/text()').extract()
	i['version'] = sel.xpath('//*[@itemprop="softwareVersion"]/text()').extract()
	i['requirementsos'] =  sel.xpath('//*[@itemprop="operatingSystems"]/text()').extract()
	i['content_rating'] = sel.xpath('//*[@itemprop="contentRating"]/text()').extract()
	i['devweb'] = sel.xpath('//*[@class="dev-link"]/@href').extract()[0]
	i['devemail'] = sel.xpath('//*[@class="dev-link"]/@href').extract()[1]
	i['score'] = sel.xpath('//*[@class="score"]/text()').extract()
	i['reviewsnum'] = sel.xpath('//*[@class="reviews-num"]/text()').extract()
	i['star5num'] =  sel.xpath('//*[@class="rating-bar-container five"]/span[3]/text()').extract()
	i['star4num'] =  sel.xpath('//*[@class="rating-bar-container four"]/span[3]/text()').extract()
	i['star3num'] =  sel.xpath('//*[@class="rating-bar-container three"]/span[3]/text()').extract()
	i['star2num'] =  sel.xpath('//*[@class="rating-bar-container two"]/span[3]/text()').extract()
	i['star1num'] =  sel.xpath('//*[@class="rating-bar-container one"]/span[3]/text()').extract()

	items.append(i)


	for a in items:
     	    print a	

	return items
 
