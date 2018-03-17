from collections import defaultdict
from collections import Counter
from collections import OrderedDict

#使用setdefault和defaultdict处理缺失的键
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon', 12)	#不存在的键
print(carbon)
print(periodic_table)
helium = periodic_table.setdefault('Helium',947)	#存在的键
print(helium)
print(periodic_table)

periodic_table = defaultdict(int)		#不存在的键值默认为0
print(periodic_table['Lead'])
print(periodic_table)

def no_idea():
	return 'Huh?'
bestiary = defaultdict(no_idea)			#defaultdict返回函数值
bestiary['A'] = 'Abominable Snowan'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

food_counter = defaultdict(int)			#使用int作为计数器
for food in ['spam', 'spam', 'eggs', 'spam']:
	food_counter[food] += 1
for food, count in food_counter.items():
	print(food, count)

#使用count计数
breakfast = ['spam', 'spam','eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())		#降序
print(breakfast_counter.most_common(1))		#显示给定数字前的元素

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(breakfast_counter + lunch_counter)	#相加
print(breakfast_counter - lunch_counter)	#从一个计数器中去掉另一个
print(breakfast_counter & lunch_counter)	#交集
print(breakfast_counter | lunch_counter)	#并集，相同项取最大

#使用有序字典OrderedDict按键排序
quotes = OrderedDict([
	('Moe', 'A wise guy'),
	('Larry', 'Ow!'),
	('Curly', 'nyuk!')
])
for stooge in quotes:
	print(stooge)

