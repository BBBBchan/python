import requests
url = 'http://www.google.com'
resp = requests.get(url)
print(resp.text)