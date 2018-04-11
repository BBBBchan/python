import requests

url1 = 'http://pythonscraping.com/pages/page1.html'
url2 = 'http://www.baidu.com'
html = requests.get(url1)
print(html.text)