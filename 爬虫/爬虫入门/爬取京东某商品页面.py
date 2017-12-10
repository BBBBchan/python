import requests
url = "https://item.jd.com/4824715.html"
try:
	r = requests.get(url,timeout=5)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("失败")