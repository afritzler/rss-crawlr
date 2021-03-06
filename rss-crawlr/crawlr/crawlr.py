from config import Config
from cassandra.cluster import Cluster
import feedparser
import redis
import os


class Crawlr:

    def __init__(self, rss_feed_file):
        self.config_file = rss_feed_file
        print "Creating redis cache connection ..."
        self.cache = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'localhost'),
                                       port=os.getenv('REDIS_POST', 6379),
                                       db=0)
        print "Creating cassandra cluster connection ..."
        self.cluster = Cluster([os.getenv('CASSANDRA _HOST', 'localhost')])

    def initialize_cache(self):
        return self.cache

    def initialize_database(self):
        return self.cluster

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