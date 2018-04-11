import requests
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page1.html'
html = requests.get(url)
bsObj = BeautifulSoup(html.text, 'html.parser')
print(bsObj.h1)
