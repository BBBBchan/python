# import sys
# type = sys.getfilesystemencoding()
# print mystr.decode('utf-8').encode(type)
import requests  
url = 'http://www.baidu.com'
html = requests.get(url)
html.encoding = 'utf8'
print (html.text)