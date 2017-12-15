import requests
from bs4 import BeautifulSoup
try:
	url = 'http://www.baidu.com'
	r = requests.get(url,timeout = 5)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	temp = r.text
	soup = BeautifulSoup(temp,"html.parser")
	print(soup.prettify())
except:
	print(错误)
