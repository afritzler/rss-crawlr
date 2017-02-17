import yaml

class Crawlr:

    config_file = "./test_config"

    def __init__(self, rss_feed_file):
        self.config_file = rss_feed_file

    def read_config(self):
        with open(self.config_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        for section in cfg:
            print(section)

        return True

    def start(self):
        read_config()

        return "Crawling ..."