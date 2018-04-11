import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'

html = requests.get(url)
bsObj = BeautifulSoup(html.text, 'html.parser')

namelist = bsObj.findAll('span', {'class':'green'})

for name in namelist:
	print(name.get_text())