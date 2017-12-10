import requests
import os
url = "http://f.hiphotos.baidu.com/image/h%3D220/sign=e881f9e8efdde711f8d244f497edcef4/3ac79f3df8dcd1008742b1cc788b4710b8122f04.jpg"
root = "E://爬取图片//"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url,timeout=5)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")	
except:
	print("爬取失败")