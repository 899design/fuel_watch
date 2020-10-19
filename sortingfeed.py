import requests
import feedparser
import pprint
from pprint import pprint


def list_date(today_tomorrow):
    current_feed = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Byford'+str(today_tomorrow))
    return current_feed ['entries']


today = ''
tomorrow = '&Day=tomorrow'
yesterday = '&Day=yesterday'

# lists
today_prices = list_date(today)
to_prices = list_date(tomorrow)
yd_prices = list_date(yesterday)

# Lists 2
unleaded_today = dict.fromkeys(today_prices,['location'])



print ('space test')
pprint (unleaded_today)
print ('space test')


for entry in today_prices:
    print(entry.date +' ' + entry.location + ' ' + entry.price + ' ' + entry.address)
print ()
pprint ('TOMORROW') 
for entry in to_prices:

    print(entry.date +' ' + entry.location + ' ' + entry.price + ' ' + entry.address)

print ()
pprint ('YESTERDAY') 
for entry in yd_prices:

    print(entry.location + ' ' + entry.price + ' ' + entry.address)

print ()
#sorted_feed = sorted(entries,['price'])

def by_price(item):
   return item['price']

today_prices = sorted(today_prices, key=by_price)
print ('SORTED DATA')
#pprint(today_prices)


