import requests
import feedparser
import pprint
from pprint import pprint


def list_date(today_tomorrow):
    current_feed = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Karratha'+str(today_tomorrow))
    return current_feed ['entries']


today = ''
tomorrow = '&Day=tomorrow'
yesterday = '&Day=yesterday'

today_prices = list_date(today)
to_prices = list_date(tomorrow)
yd_prices = list_date(yesterday)


FileNotFoundError