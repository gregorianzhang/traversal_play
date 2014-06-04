# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TraversalPlayItem(Item):
    # define the fields for your item here like:
    # name = Field()
    url = Field()
    md5 = Field()
    name = Field()
    devid = Field()
    icon = Field()
    appid = Field()
    images = Field()
    description = Field()
    category = Field()
    whatsnew = Field()
    star = Field()
    comment = Field()
    datepublished = Field()
    filesize = Field()
    numdownload = Field()
    version = Field()
    requirementsos = Field()
    content_rating = Field()
    devemail = Field()
    devweb = Field()
    score = Field()
    reviewsnum = Field()
    star5num = Field()
    star4num = Field()
    star3num = Field()
    star2num = Field()
    star1num = Field()

