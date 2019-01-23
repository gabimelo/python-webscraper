import requests
from bs4 import BeautifulSoup

URL = "https://www.coindesk.com/price/"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
latest = soup.find('div', attrs = {'class':'latest'}).span.contents[0].encode('utf-8')

print 'Current Bitcoin prince, in USD, is ${}'.format(latest)

# while value is not actually being loaded by scraping, as it's dynamically loaded onto the page, let's just get it from their API
URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(URL)

import json 
json_data = json.loads(r.content)
latest = json_data["bpi"]["USD"]["rate_float"]

print 'Current Bitcoin prince, in USD, is ${}'.format(latest)