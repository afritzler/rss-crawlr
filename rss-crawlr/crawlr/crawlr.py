from config import Config
import feedparser


class Crawlr:

    def __init__(self, rss_feed_file):
        self.config_file = rss_feed_file

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