import requests  
url = 'http://www.baidu.com'
html = requests.get(url)
html.encoding = 'utf8'
print html.text