# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from scrapy import log

from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline

from traversal_play.items import TraversalPlayItem
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')


class TraversalPlayPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'market',
            user = 'root',
            passwd = 'root',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )

    def handle_error(self, e):
        log.err(e)


    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        if item.get('url'):
	    whatsnew = '\n'.join(str(n) for n in item['whatsnew'])
            tx.execute("insert into googleplay (url,md5,name,devid,icon,images,category,whatsnew,datepublished,filesize,numdownload,version,requirementsos,devemail,devweb,score,content_rating,star1num,star2num,star3num,star4num,star5num,reviewsnum) values (%s, %s, %s, %s ,%s ,%s, %s, %s, %s ,%s ,%s, %s, %s, %s ,%s ,%s, %s, %s, %s ,%s ,%s, %s, %s)",
                (item['url'],
                 item['md5'],
                 item['name'][0],
                 item['devid'][0],
                 item['icon'][0],
                 item['images'][0],
                 item['category'],
#                 item['whatsnew'][0],
		 whatsnew,		
                 item['datepublished'][0],
                 item['filesize'][0],
                 item['numdownload'][0],
                 item['version'][0],
                 item['requirementsos'][0],
                 item['devemail'],
                 item['devweb'],
                 item['score'][0],
                 item['content_rating'][0],
                 item['star1num'][0],
                 item['star2num'][0],
                 item['star3num'][0],
                 item['star4num'][0],
                 item['star5num'][0],
                 item['reviewsnum'][0],
                )
                )

