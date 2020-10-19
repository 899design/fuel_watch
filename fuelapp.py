import requests


import feedparser

# feed1 = feedparser.parse(response.content)
# print(feed1)
#
import feedparser
from pprint import pprint

feed1 = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Karratha')

pprint(feed1)
