import requests
import feedparser
import pprint
current_feed = []
current_feed = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Karratha')
current_feed = current_feed['entries']
print (current_feed[0]['title'])
print (current_feed[0]['brand'])


#def by(ite):
 #   print(ite,type(ite))
  #  return ite[0]

#most_expensive = sorted (current_feed, key=entry.price)

#pprint.pprint(most_expensive)