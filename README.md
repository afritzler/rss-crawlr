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
Setup your `virtualenv` for this project
```
virtualenv -f rss-crawlr/requirements.txt venv
source venv/bin/activate
```
Configure the feeds you want to crawl
```
cp rss-crawlr/config/crawlr.conf.sample rss-crawlr/config/crawlr.conf
```
Adjust the `crawlr.conf` to your needs and run the local server 
```
cd rss-crawlr
python server.py config/crawlr.conf
```
To stop and remove the dockerized Redis and Cassandra container run:
```
./utils/stop_services.sh
```

# Local development using Vagrant

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
