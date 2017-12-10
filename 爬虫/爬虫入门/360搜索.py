import requests
try:
	url = "http://www.so.com/s"
	kv = {'q': 'BB'}
	r = requests.get(url,params = kv)
	r.raise_for_status()
	print(r.request.url)
	print(r.status_code)
	print(len(r.text))
except:
	print("错误")
#模拟360搜索