def menu1(wine, entree, dessert):
	return{'wine':wine, 'entree':entree, 'dessert':dessert}

print(menu1('chardonnay', 'chicken', 'cake'))#位置参数
print(menu1(wine = 'chardonnay', entree = 'chicken', dessert = 'cake'))#关键字参数
print(menu1('frontenac', dessert = 'flan', entree = 'fish')) #混合使用

def menu2(wine, entree, dessert = 'pudding'):				#指定默认参数值
	return{'wine':wine, 'entree':entree, 'dessert':dessert}

print(menu2('chardonnay', 'chicken'))

def buggy1(arg, result = []):	#result只重置一次
	result.append(arg)
	print(result)
buggy1('a')
buggy1('b')

def buggy2(arg):		#每次都被重置
	result = []
	result.append(arg)
	print(result)
buggy2('a')
buggy2('b')

def nonbuggy(arg, result = None):
	if result is None:
		result = []
	result.append(arg)
	return result
nonbuggy('a')
nonbuggy('b')

#使用*收集位置参数
def print_args(*args):
	print('Positional argument tuple:', args)
print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
	print('Need this one:', required1)
	print('Need this one too:', required2)
	print('All the rest:',args)
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

#使用**收集关键字参数
def print_kwargs(**kwargs):
	print('Keyboard arguments:', kwargs)
print_kwargs(wine = 'merlot', entree = 'mutten', dessert = 'macaroon')

#文档字符串
def echo(anything):
	'echo returns its input argument'
	return anything
help(echo)

def print_if_true(thing, check):
	'''
	Prints the first argument if a second argument is true.
	The operation is:
	1.Check whether the *second* argument is true.
	2.If it is, print the *first* argument.
	'''
	if check:
		print(thing)
print(print_if_true.__doc__)

#骚皮操作,类似函数的迭代,作为参数的函数
def answer():
	print(100)
def run_something(func):
	func()
run_something(answer)

def add_args(arg1, arg2):
	print(arg1 + arg2)
def run_spmething_with_args(func, arg1, arg2):
	func(arg1, arg2)
run_spmething_with_args(add_args, 5, 9)

def sum_args(*args):
	return sum(args)
def run_with_positional_args(func, *args):
	return func(*args)
print(run_with_positional_args(sum_args, 1, 2, 3, 4))

#内部函数
def outer(a, b):
	def inner(c, d):
		return c + d
	return inner(a, b)
print(outer(4, 7))

def knights(saying):
	def inner(quote):
		return "We are the knights who says: '%s'" % quote
	return inner(saying)
print(knights('Ni!'))

#函数闭包
def knights2(saying):
	def inner2():
		return "We are the knights who says: '%s'" % saying
	return inner2
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a)
print(b)
print(type(a))
print(type(b))
print(a())
print(b())

#lambda()函数
def edit_story(words, func):
	for word in words:
		print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
	return word.capitalize() + '!'
edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')

#生成器
def my_range(first=0, last=0, step=1):		#自制的range函数
	number = first
	while number < last:
		yield number
		number+=step
print(my_range)				#类型      
ranger = my_range(1,5)
print(ranger)				#返回生成器对象
for x in ranger:			#使用
	print(x)

#装饰器
def document_it(func):				#定义一个装饰器
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function

def add_ints(a, b):
	return a + b
print(add_ints(3,5))
cooler_add_int = document_it(add_ints)		#使用装饰器
print(cooler_add_int(3,5))

@document_it			#添加装饰器
def add_int(a,b):
	return a+b
print(add_int(3,5))

def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		return result*result
	return new_function
#使用多个装饰器的顺序
@document_it
@square_it
def add_ints(a,b):
	return a+b
print(add_i
	nts(3,5))

@square_it
@document_it
def add_ints(a,b):
	return a+b
print(add_ints(3,5))
