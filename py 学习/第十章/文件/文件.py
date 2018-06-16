import os
import shutil
# fout = open('oops.txt', 'wt')
# print('Oops, I created a file.', file=fout)
# fout.close()

#检查文件是否存在
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))

#检查是否为文件
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('.'))		#当前目录
print(os.path.isdir('..'))		#上级目录

#检查路径
print(os.path.isabs(name))
print(os.path.isabs('/big/name'))
print(os.path.isabs('name/big'))		#必须由/开始

#复制、移动、重命名文件
shutil.copy('oops.txt', 'ohho.txt')
shutil.move('ohho.txt', 'ohno.txt')
# os.rename('ohno.txt','ohwell.txt')

#创建链接
#os.link('oops.txt', 'yikes.txt')		#硬链接
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))		#不是符号链接
os.symlink('oops.txt','jeepers.txt')
print(os.path.islink('jeepers.txt'))	#是符号链接

#获取文件路径名和负号路径名
print(os.path.abspath('oops.txt'))
print(os.path.realpath('jeepers.txt'))

#删除文件
os.remove('oops.txt')
os.path.exists('oops.txt')