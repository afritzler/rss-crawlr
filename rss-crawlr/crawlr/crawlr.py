from config import Config

class Crawlr:

    def __init__(self, rss_feed_file):
        self.config_file = rss_feed_file

    def start(self):
        print "Starting crawlr ..."
        config = Config(self.config_file)
        print config.get_refresh_rate()

        return "Crawling ..."