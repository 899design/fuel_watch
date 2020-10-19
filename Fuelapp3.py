import requests
import feedparser
import pprint
#import datautil.parser

rss_urls = [
    'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Karratha',
    'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Karratha&Day=tomorrow',
]
current_feed = []
for url in rss_urls:
    current_feed = feedparser.parse(rss_urls)
#current_feed = (feedparser.parse(rss_urls))
    current_feed = current_feed['entries']
print (current_feed[0]['title'])
#print (current_feed[0]['brand'])

#sort = [item for sort in feeds for item in sort]

#for entry in current_feed:
 #   pprint.pprint(entry.location + ' ' + entry.price + ' ' + entry.address)