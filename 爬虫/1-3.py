# -*- coding: utf-8 -*-
import requests
url = 'https://www.amazon.cn/gp/product/B073LZ7NTH/ref=s9_acsd_hps_bw_c_x_1_w?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-4&pf_rd_r=C47AQC922ND7FM4MZYK4&pf_rd_r=C47AQC922ND7FM4MZYK4&pf_rd_t=101&pf_rd_p=62d28cc8-3cc0-4bda-9726-d5918773c592&pf_rd_p=62d28cc8-3cc0-4bda-9726-d5918773c592&pf_rd_i=1923778071'
try:
	kv = {'User-agent':'Chrome/10'}
	r = requests.get(url, headers = kv)
	print(r.status_code)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.request.headers)
	print(r.text[1000:2000])
except:
	print("错误")	