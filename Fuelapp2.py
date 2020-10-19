import requests
import feedparser
import pprint

current_feed = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Karratha')
current_feed = current_feed['entries']
print (current_feed[0]['title'])
print (current_feed[0]['brand'])

for entry in current_feed:
    pprint.pprint(entry.location + ' ' + entry.price + ' ' + entry.address)

