import yaml


class Config:

    # main config
    config_file = "./config/crawlr.conf"

    def __init__(self, rss_feed_file):
        self.config_file = rss_feed_file
        self.cfg = self.read_config()

    def update_config(self):
        self.read_config()

    def read_config(self):
        with open(self.config_file, 'r') as ymlfile:
            try:
                self.cfg = yaml.load(ymlfile)
                for section in self.cfg:
                    print(section)
            except yaml.YAMLError as exc:
                print(exc)
                return None

        return self.cfg

    def get_refresh_rate(self):
        return self.cfg.get('refresh_rate')

    def get_feeds(self):
        return self.cfg.get('feeds')

    def get_feeds_urls(self):
        return None