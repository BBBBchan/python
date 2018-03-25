import urllib.request as ur 
url = 'http://www.google.com'
conn = ur.urlopen(url)
print(conn)

print(conn.status)			#HTTP状态码
data = conn.read()			#网页数据
print(data)

print(conn.getheader('Content-Type'))		#返回的数据格式

for key, value in conn.getheaders():
	print(key, value)