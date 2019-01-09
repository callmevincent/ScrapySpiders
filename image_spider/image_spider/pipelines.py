# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class FilePipeline(object):
    # to save the items to an intended file.
    def __init__(self):
        self.file = open(file='images.txt', mode='ab+')

    def process_item(self, item, spider):
        print(type(spider))
        url = dict(item)['img_url'] + "\n"
        self.file.write(url.encode(encoding="utf-8"))
        return item


# class MongoPipeline(object):
#     collection_name = 'scrapy_items'
#
#     # to save items to a specific mongodb collection
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#         self.client = None
#         self.db = None
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri = crawler.settings.get('MONGO_URI'),
#             mongo_db = crawler.settings.get('MONGO_DATABASE', 'items')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert_one(dict(item))
#         return item
