# rss-crawlr
Crawl RSS Feeds

# Overview

This project crawls a list of RSS feeds periodically and stores the content
in a Cassandra database.

# Configure & Run

# Local development

___Prerequisites___
* Docker daemon
* Python 2.7.x, virtualenv

Before you start `crawlr` the backend services must be present on your machine. To spin up a dockerized Redis
and Cassandra on your host run:

```
git clone https://github.com/afritzler/rss-crawlr.git
cd rss-crawlr
./utils/run_services.sh
```

## Local development using Vagrant

___Prerequisites___
* Vagrant
* VirtualBox

To run the Vagrant box:
```
git clone https://github.com/afritzler/rss-crawlr.git
cd rss-crawlr
vagrant up
```

To remove everything from your local machine run
```
vagrant destroy -f
```
