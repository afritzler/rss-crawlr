from crawlr.crawlr import Crawlr

import sys

def print_help():
    print "RSS Crawlr Usage:"
    print "\t python server.py PATH_TO_CONFIG_FILE"

if len(sys.argv) < 2:
    print_help()
    sys.exit(0)
else:
    crawlr = Crawlr(sys.argv[1])
    crawlr.start()


