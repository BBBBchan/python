bdata = bytes(range(0, 256))
fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()		   #创建并写入一个255字节的二进制文件
fin = open('bfile', 'rb')
fin.seek(-2, 2)			#读取文件结尾前一个字节
bdata = fin.read()
print(bdata)