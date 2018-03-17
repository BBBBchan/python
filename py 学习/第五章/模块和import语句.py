#导入模块
import report as wr

description = wr.get_description()
print("Today's weather:",description)

#模块搜索路径
import sys
for place in sys.path:
	print(place)