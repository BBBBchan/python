import requests
from bs4 import BeautifulSoup

def gettitle(url):
	try:
		html = requests.get(url)
	except(HTTPError, URLError) as e:
		return None
	try:
		bsObj = BeautifulSoup(html.text, 'html.parser')
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

url = 'http://pythonscraping.com/pages/page1.html'
title = gettitle(url)
if title == None:
	print('title not found')
else:
	print(title)