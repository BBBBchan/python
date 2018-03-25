menu = \
{
"breakfast":{
	"hours": "7-11",
	"items":{
		"breakfast burritors": "$6.00",
		"pancakes" : "$4.00"
		}	
	},
"lunch":{
	"hours": "11-3",
	"items":{
		"hamburger":"$5.00"
		}
	},
"dinner":{
	"hours" : "3-10",
	"items":{
	"spaghetti": "$8.00"
		}
	}
}

import json
#利用dumps()将menu编码成json字符串
menu_json = json.dumps(menu)
print(menu_json)
#使用loads()把json字符串menu_json解析成python的数据结构
menu2 = json.loads(menu_json)
print(menu2)

import datetime
now = datetime.datetime.utcnow()
print(now)
# json.dumps(now)			由于标准json没有定义日期或者时间类型,会报错

# 把datetime转换成json能理解的类型
now_str = str(now)			#转换成字符串
print(now_str)
print(json.dumps(now_str))

from time import mktime
now_epoch = int(mktime(now.timetuple()))		#转换成epoch值
print(json.dumps(now_epoch))

class DTEncoder(json.JSONDecoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):		#isinstance()检查obj类型
			return int(mktime(obj.timetuple()))
		return json.JSONDecoder.default(self, obj)	#否则是普通解码器知道的东西
json.dumps(now, cls=DTEncoder)

