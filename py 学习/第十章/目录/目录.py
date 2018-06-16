import os
import glob

#创建目录
# os.mkdir('poems')
print(os.path.exists('poems'))

#删除目录
# os.rmdir('poems')
print(os.path.exists('poems'))

#列出目录内容
#os.mkdir('poems')
print(os.listdir('poems'))
#os.mkdir('poems/mcintyre')
print(os.listdir('poems'))

#写入文件
fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('''
	Beautiful is better than ugly.
	Explicit is better than implicit.
	Simple is better than complex.
	Complex is better than complicated.
	Flat is better than nested.
	Sparse is better than dense.
	Readability counts.
	Special cases aren't special enough to break the rules.
	Although practicality beats purity.
	Errors should never pass silently.
	Unless explicitly silenced.
	In the face of ambiguity, refuse the temptation to guess.
	There should be one-- and preferably only one --obvious way to do it.
	Although that way may not be obvious at first unless you're Dutch.
	Now is better than never.
	Although never is often better than *right* now.
	If the implementation is hard to explain, it's a bad idea.
	If the implementation is easy to explain, it may be a good idea.
	Namespaces are one honking great idea -- let's do more of those!
	''')
fout.close()

#查看目录内容
print(os.listdir('poems/mcintyre'))

#改变当前目录
os.chdir('poems')

#列出匹配文件
'''
规则:
*会匹配任意名称
？匹配一个字符
[abc]匹配字符a,b和c
[!abc]匹配非abc字符
'''
print(glob.glob('m*'))
print(glob.glob('??'))
print(glob.glob('m???????'))
print(glob.glob('[klm]*e'))