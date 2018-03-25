poem = '''There was a young lady named Bright,
		Whose speed was far faster than light;
		She started one day
		In a relative way,
		And returned on the previous night.'''
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity', 'wt')
print(poem, file = fout, sep = ' ', end = ' ')
fout.close()

#将数据分块写入
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
	if offset > size:
		break
	fout.write(poem[offset:offset+chunk])
	offset += chunk
fout.close()
try:
	fout = open('relativity', 'xt')
	fout.write('stomp stomp stomp')
except FileExistsError:
	print('relativity already exists!. That was a close one.')

#使用read()读取文件
fin = open('relativity', 'rt')
poem = fin.read()				#直接读取文件的全部内容，使用内存大小与文件本身相同
fin.close()

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
	fragment = fin.read(chunk)		#每次读入100个字符
	if not fragment:
		break
	poem += fragment
fin.close()

poem = ''
fin = open('relativity', 'rt')
while True:
	line = fin.readline()			#每次读取一行
	if not line:
		break
	poem += line
fin.close()

poem = ''
fin = open('relativity', 'rt')		#使用迭代器逐行读取
for line in fin:
	poem += line
fin.close()

poem = ''
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
	print(line , end = '')

#使用write()写二进制文件
bdata = bytes(range(0, 256))
print(len(bdata))
fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

#分块写入数据
fout = open('bfile', 'wb')
offset = 0
size = len(bdata)
chunk = 100
while True:
	if offset > size:
		break
	fout.write(bdata[offset : offset+chunk])
	offset += chunk
fout.close()

#使用read()读取二进制文件
fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

#使用with自动关闭文件
# with open('relativity', 'wt') as fout:
# 	fout.write(poem)

#使用seek()改变位置
fin = open('bfile', 'rb')
print(fin.tell())
fin.seek(255)
bdata = fin.read()
print('length of bdata is', len(bdata))
print('fin.tell() is', fin.tell())
fin.close()
#关于seek()的参数
#第一个参数offset表示偏移量，第二个表示开始的位置： 0表示从文件开始，1表示从当前开始，2表示从末尾开始
import os
print(os.SEEK_SET)
print(os.SEEK_END)
print(os.SEEK_CUR)

fin = open('bfile', 'rb')
fin.seek(-2, 2)			#读取文件结尾前一个字节
bdata = fin.read()
print(bdata)

fin.seek(254, 0) 		#从文件开始找到第254位
fin.seek(1, 1)			#在254位之后再寻找一位




