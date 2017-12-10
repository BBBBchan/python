#-*- coding: UTF-8 -*- 
import urllib2
response = urllib2.urlopen("http://www.baidu.com")
response.encoding = 'utf8'
print response.read()