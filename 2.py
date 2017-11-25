#-*- coding: UTF-8 -*- 
import re

#假设下面是一个源码，我想保存里面所有的链接
text = '<a href = "www.baidu.com">....'
urls = re.findall('<a href = (.*?)>',text,re.S)
for each in urls:
    print each

#假设我需要爬取当前网页的头部
html = u'''
<html>
<title>爬虫的基本知识</title>
<body>
……
</body>
</html>
'''

print re.search('<title>(.*?)</title>',html,re.S).group(1)
#这里group(1)表示第一个括号的内容，如果正则里面有多个括号，这里可以通过group(i)返回第i个空格里的内容



#假设下面是一个贴吧的帖子地址，有很多页，每一页就是靠后面的pn=几来区分的，我们输出前10页的网址
Pages = 'http://tieba.baidu.com/p/4342201077?pn=1'

for i in range(10): 
    print re.sub('pn=\d','pn=%d'%i,Pages)

