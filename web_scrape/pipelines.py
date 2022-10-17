import pymongo
import pandas as pd
import sys
from .items import QuoteItem
from .datagen import DataGen


class MongoDBPipeline:

    collection = 'quotes'

    def __init__(self, mongodb_uri='localhost:27017', mongodb_db='web_scrapping'):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit('You need to provide connection string')
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]
        # clean database
        self.db[self.collection].delete_many({})
    
    def close_spider(self, spider):
        # Export MongoDB to pandas DataFrame
        df = pd.DataFrame(list(self.db[self.collection].find()))
        df.to_csv(
            path_or_buf='./exported.csv',
            columns=pd.Series(
                data=['author', 'text', 'tags']
            ),
        )
        DataGen()
        self.client.close()
    
    def process_item(self, item, spider):
        data = dict(QuoteItem(item))
        self.db[self.collection].insert_one(data)
        return item