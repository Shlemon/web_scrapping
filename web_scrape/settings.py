BOT_NAME = 'web_scrape'
SPIDER_MODULES = ['web_scrape.spiders']
NEWSPIDER_MODULE = 'web_scrape.spiders'
ITEM_PIPELINES = {
    "web_scrape.pipelines.MongoDBPipeline": 500
}
ROBOTSTXT_OBEY = True


MONGODB_URI = "localhost:27017"
MONGODB_DATABASE = "web_scrapping"