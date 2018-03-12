import requests
from bs4 import BeautifulSoup

URL = "https://www.last.fm/music/The+Beatles/+wiki"
r = requests.get(URL)
print r

# soup = BeautifulSoup(r.content, 'html5lib')
# latest = soup.find('div', attrs = {'class':'latest'}).span.contents[0].encode('utf-8')
