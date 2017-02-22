from config import Config
import feedparser
import redis
import os


class Crawlr:

    def __init__(self, rss_feed_file):
        self.config_file = rss_feed_file
        self.cache = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'localhost'),
                                       port=os.getenv('REDIS_POST', 6379),
                                       db=0)

    def start(self):
        print "Starting crawlr ..."
        config = Config(self.config_file)
        print config.get_refresh_rate()

        for feed in config.get_feeds():
            for feed_data in feedparser.parse(feed['url']).entries:
                print feed_data.title
                print feed_data.published
                print feed_data.link

        return "Crawling ..."