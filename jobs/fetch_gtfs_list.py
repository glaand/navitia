#!/usr/bin/env python3
import os.path
import requests
import json
from jsondiff import diff

DATA = 'data/'

# Cached data
CACHED_FEEDS = '/tmp/tpp_feeds.json'
cached_data = []
if os.path.exists(CACHED_FEEDS):
    cached_data = json.loads(open(CACHED_FEEDS, 'r').read())

# Fetched data
url = 'https://api.tpp.pt/v1/feeds'
resp = requests.get(url=url)
fetched_data = resp.json()

diff_data = json.loads(diff(cached_data, fetched_data, dump=True))
if '$replace' in diff_data:
    feeds = diff_data['$replace']['feeds']
    for feed in feeds:
        with open(DATA + feed['onestop_id'] + '.zip', "wb") as file:
            response = requests.get(feed['url'])
            file.write(response.content)
            print("Downloaded %s" % (feed['onestop_id'] + '.zip'))
    with open(CACHED_FEEDS, 'w') as outfile:
        json.dump(fetched_data, outfile)
