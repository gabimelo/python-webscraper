
import requests
from bs4 import BeautifulSoup

URL = "http://www.camara.sp.gov.br/vereador/adilson-amadeu/"
URL = "http://www.camara.sp.gov.br/vereadores/"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
print soup
# latest = soup.find('div', attrs = {'class':'latest'}).span.contents[0].encode('utf-8')

# print 'Current Bitcoin prince, in USD, is ${}'.format(latest)
